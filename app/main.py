import streamlit as st

from router import router
from faq import ingest_faq_data, faq_chain
from sql import sql_chain


# ---------------------------------------------------------
# Page configuration
# ---------------------------------------------------------
st.set_page_config(
    page_title="E-Commerce Chat-Bot",
    page_icon="🛒",
    layout="centered"
)


# ---------------------------------------------------------
# Custom CSS
# ---------------------------------------------------------
st.markdown(
    """
    <style>

    /* Main application container */
    .main .block-container {
        max-width: 900px;
        padding-top: 2rem;
        padding-bottom: 5rem;
    }

    /* Prevent long URLs/text from overflowing */
    .stChatMessage p,
    .stChatMessage a {
        overflow-wrap: anywhere !important;
        word-break: break-word !important;
        white-space: normal !important;
    }

    /* Prevent horizontal scrolling in chat messages */
    .stChatMessage {
        max-width: 100%;
        overflow-x: hidden !important;
    }

    .stChatMessage [data-testid="stMarkdownContainer"] {
        max-width: 100%;
        overflow-wrap: anywhere !important;
        word-break: break-word !important;
    }

    /* Make links wrap instead of creating horizontal scrollbars */
    .stChatMessage a {
        display: inline-block;
        max-width: 100%;
        overflow-wrap: anywhere !important;
        word-break: break-all !important;
    }

    /* Chat input */
    .stChatInputContainer {
        max-width: 900px;
    }

    /* Improve code/text blocks if present */
    .stChatMessage pre {
        max-width: 100%;
        overflow-x: auto;
    }

    </style>
    """,
    unsafe_allow_html=True
)


# ---------------------------------------------------------
# Initialize FAQ data
# ---------------------------------------------------------
@st.cache_resource
def initialize_faq():
    ingest_faq_data()
    return True


initialize_faq()


# ---------------------------------------------------------
# Initialize chat history
# ---------------------------------------------------------
if "messages" not in st.session_state:
    st.session_state["messages"] = []


# ---------------------------------------------------------
# Ask function
# ---------------------------------------------------------
def ask(query):

    try:
        route_result = router(query)
        route = route_result.name

        if route == "faq":
            response = faq_chain(query)

        elif route == "sql":
            response = sql_chain(query)

        else:
            response = f"Route '{route}' is not implemented."

        return str(response)

    except Exception as e:
        return f"Sorry, an error occurred: {e}"


# ---------------------------------------------------------
# Title
# ---------------------------------------------------------
st.title("🛒 E-Commerce Chat-Bot")


# ---------------------------------------------------------
# Greeting
# ---------------------------------------------------------
with st.chat_message("assistant"):
    st.markdown("Hello, how may I help you?")


# ---------------------------------------------------------
# Display previous conversation
# ---------------------------------------------------------
for message in st.session_state["messages"]:

    with st.chat_message(message["role"]):
        st.markdown(message["content"])


# ---------------------------------------------------------
# Chat input
# ---------------------------------------------------------
query = st.chat_input("Write your query...")


# ---------------------------------------------------------
# Process query
# ---------------------------------------------------------
if query:

    # Display user message
    with st.chat_message("user"):
        st.markdown(query)

    # Save user message
    st.session_state["messages"].append({
        "role": "user",
        "content": query
    })

    # Generate response
    response = ask(query)

    # Display assistant response
    with st.chat_message("assistant"):
        st.markdown(response)

    # Save assistant response
    st.session_state["messages"].append({
        "role": "assistant",
        "content": response
    })