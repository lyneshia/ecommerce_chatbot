# 🛒 E-Commerce Chatbot

An AI-powered e-commerce chatbot that provides a conversational
interface for answering frequently asked questions and retrieving
product information from an SQLite database. The application uses
semantic routing to determine whether a user query should be handled by
the FAQ or SQL workflow.

## ✨ Features

-   💬 Conversational chatbot interface built with Streamlit
-   🧭 Semantic routing for intelligent query classification
-   📚 FAQ question answering using vector search
-   🗄️ SQL-based product and database queries
-   🤖 LLM-powered responses using Groq
-   🔎 ChromaDB for storing and retrieving FAQ embeddings
-   🧠 Hugging Face encoder support through Semantic Router
-   💾 SQLite database for structured e-commerce data
-   📄 FAQ data maintained in CSV format
-   🔐 Environment variables for securely storing API credentials

## 🏗️ Project Structure

``` text
ecommerce_chatbot/
│
├── app/
│   ├── faq.py          # FAQ ingestion, vector search and FAQ chain
│   ├── main.py         # Streamlit application and chat interface
│   ├── router.py       # Semantic query routing
│   └── sql.py          # SQL query generation and database workflow
│
├── resources/
│   ├── db.sqlite       # SQLite database containing e-commerce data
│   └── faq_data.csv    # Frequently asked questions and answers
│
├── .gitignore
├── LICENSE
└── requirements.txt
```

## 🔄 Application Workflow

``` text
                    User Query
                        │
                        ▼
                ┌─────────────────┐
                │ Streamlit UI    │
                │    main.py      │
                └────────┬────────┘
                         │
                         ▼
                ┌─────────────────┐
                │ Semantic Router │
                │   router.py     │
                └────────┬────────┘
                         │
                ┌────────┴─────────┐
                │                  │
             FAQ Query         SQL Query
                │                  │
                ▼                  ▼
          ┌───────────┐      ┌───────────┐
          │  faq.py   │      │  sql.py   │
          │ ChromaDB  │      │ SQLite DB │
          └─────┬─────┘      └─────┬─────┘
                │                  │
                └────────┬─────────┘
                         │
                         ▼
                   Groq LLM
                         │
                         ▼
                  Chatbot Response
```

## 🧩 Main Components

### 1. `main.py`

The main Streamlit application.

Responsibilities:

-   Creates the chatbot interface
-   Maintains conversation history
-   Accepts user queries
-   Calls the semantic router
-   Sends the query to the appropriate workflow
-   Displays the generated response

Run the application with:

``` bash
streamlit run app/main.py
```

### 2. `router.py`

Uses Semantic Router to classify incoming queries.

The router determines whether the query belongs to:

-   `faq` --- questions about policies, discounts, orders, returns, etc.
-   `sql` --- questions requiring information from the e-commerce
    database

This avoids sending every query through the same workflow.

### 3. `faq.py`

Handles FAQ-related questions.

The FAQ workflow:

1.  Reads FAQ data from `resources/faq_data.csv`
2.  Creates embeddings for the FAQ content
3.  Stores/retrieves vectors using ChromaDB
4.  Finds relevant FAQ information
5.  Uses the LLM to generate a conversational answer

### 4. `sql.py`

Handles structured database queries.

The SQL workflow connects to:

``` text
resources/db.sqlite
```

It can be used for queries such as product searches and other questions
that require structured database information.

### 5. `resources/`

Contains the application's data sources:

-   `db.sqlite` --- SQLite database
-   `faq_data.csv` --- FAQ dataset

Keep these files in the expected location because the application uses
relative paths to access them.

## 🛠️ Technologies Used

  Technology        Purpose
  ----------------- ---------------------------------
  Python            Application development
  Streamlit         Chatbot web interface
  Groq              LLM-powered response generation
  Semantic Router   Query classification/routing
  ChromaDB          Vector storage and retrieval
  Pandas            Data processing
  SQLite            Structured e-commerce database
  Python-dotenv     Environment variable management

## 📦 Installation

### 1. Clone the repository

``` bash
git clone <your-repository-url>
cd ecommerce_chatbot
```

### 2. Create a virtual environment

#### Windows

``` bash
python -m venv venv
venv\Scripts\activate
```

#### macOS / Linux

``` bash
python3 -m venv venv
source venv/bin/activate
```

### 3. Install dependencies

``` bash
pip install -r requirements.txt
```

## 🔐 Environment Variables

Create a `.env` file in the project root:

``` env
GROQ_API_KEY=your_groq_api_key
```

Do not commit `.env` or expose your API key publicly.

The `.gitignore` file should include:

``` gitignore
.env
venv/
__pycache__/
```

## ▶️ Run the Application

From the project root:

``` bash
streamlit run app/main.py
```

Streamlit will start the application locally and provide a URL such as:

``` text
http://localhost:8501
```

Open the URL in your browser to interact with the chatbot.

## 💡 Example Queries

### FAQ queries

``` text
What is the return policy?
```

``` text
How can I track my order?
```

``` text
Do I get a discount with an HDFC credit card?
```

### Product / SQL queries

``` text
Show me some products.
```

``` text
Give me the names of available products.
```

``` text
Find products under a specific price.
```

The semantic router determines the appropriate workflow before
processing the query.

## ☁️ Streamlit Cloud Deployment

### 1. Push the project to GitHub

Make sure the repository contains:

``` text
app/
resources/
requirements.txt
.gitignore
LICENSE
```

### 2. Configure dependencies

Your `requirements.txt` should contain the packages required by the
application.

Example:

``` text
chromadb==1.5.9
groq==1.7.0
pandas==3.0.6
python-dotenv==1.2.3
semantic-router[local]==0.1.16
streamlit==1.45.1
```

### 3. Add the Groq API key

In Streamlit Cloud, add the API key through the application's Secrets
configuration rather than committing it to GitHub.

Example:

``` toml
GROQ_API_KEY = "your_groq_api_key"
```

The application can then access it through the environment or Streamlit
secrets, depending on how the application code is configured.

### 4. Set the main file

Use:

``` text
app/main.py
```

as the Streamlit entry point.

## ⚠️ Important Deployment Notes

-   Keep `resources/db.sqlite` in the repository if the deployed
    application needs the bundled database.
-   Keep `resources/faq_data.csv` in the repository.
-   Do not commit API keys or `.env` files.
-   Make sure file paths are relative to the project root or otherwise
    resolved consistently.
-   If ChromaDB creates a local persistent directory during execution,
    remember that Streamlit Cloud storage is not intended to be
    permanent application storage.
-   Pin package versions in `requirements.txt` to reduce
    dependency-related deployment issues.

## 🔒 Security

Never hard-code credentials such as:

``` python
GROQ_API_KEY = "gsk_..."
```

Instead, use environment variables or Streamlit secrets.

For local development:

``` env
GROQ_API_KEY=your_groq_api_key
```

For Streamlit Cloud, configure the secret through the platform.

## 🚀 Future Improvements

Potential enhancements include:

-   Product recommendation functionality
-   Order-status lookup using an order ID
-   Conversation-aware product search
-   Product filtering by category, price, and rating
-   Chat history persistence
-   User authentication
-   Improved response formatting with product cards
-   Deployment using a hosted database instead of SQLite
-   Evaluation of router accuracy and FAQ retrieval quality

## 📄 License

This project is distributed under the license included in the `LICENSE`
file.

------------------------------------------------------------------------

## 👩‍💻 Author

Developed as an AI/GenAI e-commerce chatbot project demonstrating:

-   Large Language Models
-   Semantic Routing
-   Retrieval-Augmented Generation concepts
-   Vector Databases
-   SQL-based question answering
-   Streamlit application development
