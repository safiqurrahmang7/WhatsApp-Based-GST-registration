# GST BOT

## Project Overview

The **GST BOT** is designed to provide information and answer questions related to the Goods and Services Tax (GST) registration process. The bot utilizes an AI model to retrieve context-specific answers from a web page and uses a pre-trained model for generating relevant and concise responses.

## Instructions

### Select a Project
- Chosen Project: **GST BOT**

### Provide a Detailed Plan

#### Approach:
- **Step 1:** Load content from a specific webpage related to GST registration using a web scraper (WebBaseLoader).
- **Step 2:** Split the loaded content into smaller chunks for efficient processing.
- **Step 3:** Filter out any irrelevant or complex metadata from the document chunks.
- **Step 4:** Store the processed data in a vector store (FAISS) to enable fast similarity search.
- **Step 5:** Accept user input questions and retrieve relevant information from the vector store.
- **Step 6:** Use the GPT model to generate an accurate and context-specific response to the user's query.
- **Step 7:** Display the answer to the user in a user-friendly interface (Streamlit).

#### Technology Choices:
- **Programming Language:** Python
  - **Reason:** Python is a versatile and powerful language for AI, machine learning, and web scraping tasks.
- **Libraries & Tools:**
  - **Langchain:** Used to handle document loading, text splitting, and context extraction.
  - **FAISS:** For vector-based similarity search, ensuring fast and efficient retrieval of relevant content.
  - **OllamaLLM:** To process and generate responses based on user input.
  - **Streamlit:** Provides an easy-to-use framework to deploy and interact with the chatbot through a web interface.
  - **WebBaseLoader:** To scrape content from a web page.

#### Solution Design:
- **Data Source:** The project scrapes content from a public webpage about GST registration. This data is preprocessed and stored in a vector store (FAISS).
- **Model Type:** A retrieval-based model, using vector search for context matching, and GPT model for generating responses.
- **Workflow Structure:** 
  - Web scraping → Text processing → Vector embedding → User query → Retrieval & Response generation.

#### Challenges and Solutions:
- **Challenge 1:** Handling ambiguous or unclear user queries.
  - **Solution:** Implement fallback responses when the chatbot cannot provide an answer, such as "I don't know" or suggesting related topics.
  
- **Challenge 2:** Ensuring the relevance of the retrieved data.
  - **Solution:** Use a robust similarity search with FAISS to ensure that the most relevant context is selected for answering user queries.
  
- **Challenge 3:** Ensuring real-time responsiveness of the bot.
  - **Solution:** Optimize the retrieval process by fine-tuning vector embeddings and using efficient indexing with FAISS.

#### Assumptions:
- The user will ask questions based on the information available on the specified GST registration page.
- The bot will only be able to answer based on the information retrieved from the content it has processed.

#### Code/Workflow/POC:
- **Code Sample:** Refer to the main script for complete implementation.
- **Workflow Diagram:**
  - **Step 1:** Scrape content → **Step 2:** Split content → **Step 3:** Store in FAISS → **Step 4:** Retrieve relevant context → **Step 5:** Generate response using GPT.

### Past Experience and Relevant Knowledge
- Previous experience with **Python**, **Streamlit**, **FAISS**, and **Langchain** libraries has been useful in creating the GST BOT.
- Previous projects in machine learning have provided insight into how to manage text data and how to fine-tune models for question-answering tasks.


