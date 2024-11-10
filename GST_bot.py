from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_ollama import OllamaLLM
import streamlit as st
from langchain_community.document_loaders import WebBaseLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.vectorstores.utils import filter_complex_metadata
from langchain_community.vectorstores import Chroma
from langchain.schema.runnable import RunnablePassthrough
from langchain_community.embeddings import FastEmbedEmbeddings
import faiss
from langchain_community.docstore.in_memory import InMemoryDocstore
from langchain_community.vectorstores import FAISS
import numpy as np
from langchain_core.embeddings import FakeEmbeddings

embeddings = FakeEmbeddings(size=4096)

# Use WebBaseLoader to load content from a webpage
docs = WebBaseLoader('https://www.bankbazaar.com/tax/gst-registration.html').load()

# Split the loaded document into smaller chunks
chunks = RecursiveCharacterTextSplitter(chunk_size=1024, chunk_overlap=100).split_documents(docs)

# Filter out complex metadata from the chunks
chunks = filter_complex_metadata(chunks)

index = faiss.IndexFlatL2(len(embeddings.embed_query("hello world")))

vector_store = FAISS(
    embedding_function=embeddings,
    index=index,
    docstore=InMemoryDocstore(),
    index_to_docstore_id={},
)

# Add the embeddings to the index


st.title("GST BOT")
Question = st.text_input("Enter The Questions Here.....")

prompt = ChatPromptTemplate.from_template(
    """
    <s> [INST]You are an assistant providing guidance on the Goods and Services Tax (GST) registration process, 
    aiming to simplify the experience for individuals and small businesses. Use the following context to answer 
    the user's question clearly and concisely. If you don't know the answer, just say "I don't know." Your response 
    should help the user understand the necessary steps, documents, and procedures involved in GST registration. 
    Keep the answer within three sentences.[/INST] </s> 
    [INST] Question: {question} 
    Context: {context} 
    Answer: [/INST]
    """
)

model = OllamaLLM(model= 'mistral')
parser = StrOutputParser()




if Question:
    # Get relevant context from the vector store
    context = vector_store.similarity_search(Question, k=1)

    # Format the prompt with the context and question
    formatted_prompt = prompt.format(question=Question, context=context)

    # Get the response from the model
    raw_answer = model.invoke(formatted_prompt)

    # Parse and display the response
    answer = parser.parse(raw_answer)
    st.write(answer)



