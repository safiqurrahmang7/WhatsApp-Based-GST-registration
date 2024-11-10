# GST BOT

## Overview

**GST BOT** is an AI-powered chatbot that provides guidance on the Goods and Services Tax (GST) registration process. The bot is designed to simplify the experience for individuals and small businesses by answering questions based on the context extracted from a webpage about GST registration. Built using Langchain, FAISS, and Streamlit, the bot uses natural language processing and embeddings to understand and respond to user queries.

---

## Features

- **Context-based answers:** The bot uses the relevant content from a webpage to answer user questions clearly and concisely.
- **Integration with Langchain:** Langchain is used for building the prompt and processing the response.
- **FAISS-based vector store:** A FAISS-based vector store stores and retrieves the most relevant context for answering questions.
- **Web scraping:** Content is fetched from a webpage using the `WebBaseLoader` from Langchain.
- **Streamlit Interface:** A simple interface is created using Streamlit, where users can input their questions about GST registration.

---

## Technologies Used

- **Langchain:** For prompt building, parsing, and chaining components.
- **FAISS:** For efficient similarity search and indexing.
- **OllamaLLM:** Language model used for generating responses.
- **Streamlit:** For creating a simple, interactive web interface.
- **WebBaseLoader:** To scrape content from an external webpage.
- **FAKE embeddings:** Fake embeddings are used for illustration and can be replaced with real embeddings.
- **NumPy:** For handling numerical data related to the embeddings and FAISS operations.

---

## Setup

### Prerequisites

Before you begin, ensure you have the following installed:

- Python 3.x
- pip (Python package manager)

### Installation Steps

1. **Clone the repository:**

    ```bash
    git clone <repository-url>
    cd <project-directory>
    ```

2. **Install required dependencies:**

    ```bash
    pip install -r requirements.txt
    ```

3. **Run the application:**

    ```bash
    streamlit run app.py
    ```

This will open the application in your web browser, where you can interact with the GST BOT.

---

## How It Works

1. **Loading the Web Content:** The bot first loads content from the [GST Registration](https://www.bankbazaar.com/tax/gst-registration.html) webpage using Langchain's `WebBaseLoader`.
   
2. **Document Chunking and Preprocessing:** The loaded document is split into smaller chunks of text using the `RecursiveCharacterTextSplitter` for better processing and response accuracy.

3. **Indexing with FAISS:** The content chunks are then indexed using FAISS. Each chunk is associated with an embedding vector created using the `FakeEmbeddings` class, though this can be replaced with real embeddings.

4. **Query Processing:** When a user asks a question, the bot performs a similarity search to find the most relevant context from the indexed document. This context is combined with the user's query and passed to the `OllamaLLM` model.

5. **Generating the Response:** The model generates a response based on the question and context, which is then parsed and displayed to the user.

---

## Usage

1. Open the application in a browser after running it through Streamlit.
2. Enter a question related to **GST Registration** in the input box.
3. The bot will return a concise answer based on the context extracted from the webpage.

---

## Example Interaction

- **User Input:** "What documents are needed for GST registration?"
- **Bot Response:** "To register for GST, you need documents like proof of identity, proof of address, and bank account details. Ensure that all documents are valid and up to date."

---

## Contributing

Feel free to fork the repository, submit issues, and contribute to the development of this project. If you have suggestions or improvements, open a pull request, and I will review it.

---

## License

This project is open source and available under the [MIT License](LICENSE).

---

## Author

**Safiqur Rahman**  
[LinkedIn Profile](https://www.linkedin.com/in/safiqur-rahman)  
[GitHub Profile](https://github.com/safiqur-rahman)
