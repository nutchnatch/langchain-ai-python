# langchain-python

https://realpython.com/build-llm-rag-chatbot-with-langchain/

rag:
https://tomstechacademy.com/build-a-chatbot-with-rag-retrieval-augmented-generation/



# Build a Chatbot with RAG (Retrieval Augmented Generation)

### Do you want to build a chatbot which can answer questions based on knowledge you provide? One of the biggest challenges when working with Large Language Models is that LLM-generated answers are often too generic and LLM’s don’t have any knowledge about your business.
Retrieval Augmented Generation (RAG) solves this issue! The chatbot which we’re going to build in this tutorial will perform a vector search on every question ## asked by the user. It will use the information from the vector database to answer the question from the user and provide the answer via the chatbot.

## Architecture
In this article I describe how you can build a simple chatbot that uses RAG. For this we will be using two Python scripts:

ingest_database.py: you only need to run this script once, as it will take a PDF file (the knowledge base), cut it in small chunks and ingest it in the database.
chatbot.py: this is the actual chatbot. You can run it as many times as you want, after you have executed ingest_database.py to fill the semantic database

## How does Retrieval Augmented Generation (RAG) work?
Let’s first take a look at the part of our script which is stored in ingest_database.py. We call this the indexing. In the below picture (source: LangChain website) the four stages of indexing are described:

Load: we load a data source into our script. This can be a PDF file, an Excel file, but also a website which is scraped for example. In the load phase, the data source is loaded into the Python script.
Split: in the second phase, we split the document in smaller parts. It’s easy to imagine that in order to answer a question, the chatbot only needs to access a few phrases from the document. LLM’s are still limited to a context window, and charge based on the amount of tokens processed. So we definitely want to avoid it to parse the entire document. We only want to feed it phrases which are relevant to the question. During the splitting (chunking) process we split the document in smaller parts of about 300 characters.
Embed: for every chunk (this is how we call the parts from the document), a model will calculate the embeddings. This is mathematical representation of the phrase and can be used to calculate the similarity of two phrases (during the retrieval process we’ll use this to find phrases which are similar to the question the user asks to the chatbot).
Store: the phrases are ingested into a semantic database. In this example we’ll use Chroma.


We now have a database where we stored the document (but in smaller chunks). The chatbot will use this database to find relevant phrases to answer the questions from the users. Let’s see how that works!

Retrieval: the retrieval part is quite simple. Even before we provide the question of the user to the LLM, we provide it to the database and use the calculated embeddings to find phrases which are similar to the user’s question.
Generation: the results from the previous step (phrases which seem similar to the question) are now passed to the LLM together with the question from the user and the prompt. We’ll ask the LLM to answer the user’s question – using the results from the semantic database.



## Preparation
If you want to build this script together with me, make sure that you have the following:

Python and VS Code are installed on your system
You have access to an OpenAI API Key (click here to learn how to get it)


### 1. Install the necessary libraries
In order to install the necessary libraries, we’re going to run the following command in VS Code:
- pip install langchain_community langchain_text_splitters langchain_openai langchain_chroma gradio python-dotenv pypdf

### 2. Download and save the PDF file
Click here to download the PDF file here and save it in the directory data

### 3. Download the Python scripts:
- OPENAI_API_KEY = "[YOUR API KEY HERE]"

