from pathlib import Path
import pandas as pd
import chromadb
from groq import Groq
from dotenv import load_dotenv
import os
import streamlit as st

load_dotenv()


path = Path(__file__).parent.parent / "resources" / "faq_data.csv"
chroma_client = chromadb.Client()
collection_name = "faqs"
GROQ_API_KEY = st.secrets["GROQ_API_KEY"]
GROQ_MODEL_NAME = st.secrets["GROQ_MODEL_NAME"]
groq_client = Groq(api_key=GROQ_API_KEY)


def ingest_faq_data():
    if collection_name not in chroma_client.list_collections():
        try:
            df = pd.read_csv(path)
            collection = chroma_client.get_or_create_collection(
                name = collection_name,
            )
            doc = df['question'].tolist()
            md = [{"answer": ans} for ans in df['answer'].tolist()]
            id = [ f"id_{i}" for i in range(len(doc))]

            collection.add(
                documents=doc,
                metadatas=md,
                ids = id
            )
            print("FAQ data successfully ingested in {}".format(collection_name))
        except Exception as e:
            print("Unable to ingest faq data",e)
    else:
        print("Collection already exists")

def get_relevant_faq_data(query):
    collection = chroma_client.get_or_create_collection(name = collection_name)
    result = collection.query(
        query_texts=[query],
        n_results=2
    )
    return result

def faq_chain(query):
    result = get_relevant_faq_data(query)
    context = ''.join([ r.get('answer')for r in result['metadatas'][0]])
    answer = generate_answer(query, context)
    return answer

def generate_answer(query,context):
    prompt = f'''Get the question and context below, generate the answer. 
    Generate the answer based on the context only. If you don't find the answer in the context, then say that you don't know the answer. 
    Do not make things up
    
    Question - {query}
    Context - {context}
    '''
    try:
        chat_completion = groq_client.chat.completions.create(
            messages=[
                {
                "role": "user",
                "content": prompt
                }
            ],
            model = GROQ_MODEL_NAME
        )
    except Exception as e:
        print("Unable to generate answer",e)
    return chat_completion.choices[0].message.content
