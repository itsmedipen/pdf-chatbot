# PDF Chatbot with LangChain, Groq API & Streamlit

This project builds a chatbot that can answer questions based on the content of an uploaded PDF(single only). It uses LangChain for the retrieval-based question answering pipeline, the Groq API to power the LLaMA3 model, and Streamlit for a user-friendly interface.

## Features

- **PDF Upload:** Load a PDF document and extract the whole text.
- **Split the chunk:** Split the chunks with same size
- **Embedding:** Embedding each chunks 
- **vectorstore:** Create a vector store 
- **Question Answering:** Ask natural language questions based on the PDF content.
- **RetrievalQA Pipeline:** Uses a vector database for semantic similarity search and a custom chain to feed the retrieved context along with your question to the LLM.
- **Streamlit UI:** Simple web interface to interact with the chatbot.

## How It Works

1. **PDF Processing:**
   - The PDF is split into chunks.
   - Each chunk is embedded using a HuggingFace model and stored in a vector database (e.g., FAISS).

2. **User Interaction:**
   - The user types a question into the Streamlit interface.
   - A retriever searches for the most relevant chunks in the vector store.
   - Both the question and the context are passed to the LLM (powered by the Groq API via the LLaMA3 model).
   - The LLM generates an answer, which is displayed in the UI.

3. **Environment & Configuration:**
   - Sensitive information like the **Groq API Key** is stored in a `.env` file.
   - The `.env` file is added to `.gitignore` to ensure it is **not pushed** to GitHub.
   - An example file (`.env.example`) is provided to illustrate which environment variables are needed.

## Installation

1. **Clone the Repository:**

    ```bash
    git clone https://github.com/yourusername/pdf-chatbot.git
    cd pdf-chatbot
    ```

2. **Create & Activate a Virtual Environment:**

    ```bash
    python -m venv venv
    source venv/bin/activate    # On Windows use `venv\Scripts\activate`
    ```

3. **Install Dependencies:**

    ```bash
    pip install -r requirements.txt
    ```

4. **Configure Environment Variables:**

    - Copy `.env.example` to `.env`:

      ```bash
      cp .env.example .env
      ```

    - Open `.env` and replace `your-groq-api-key-here` with your actual Groq API key.

## Running the Application

1. **Start the Streamlit App:**

    ```bash
    streamlit run app.py
    ```

2. **Using the Chatbot:**
   - Upload your PDF file.
   - Type a question into the text box and press Enter.
   - The chatbot will use the RetrievalQA process to return an answer based on the PDF content.

## File Structure

pdf-chatbot/
├── app.py                  
├── README.md                
├── .gitignore               
├── .env.example             
├── requirements.txt         
├── config.toml              
├── .streamlit/            
│   └── config.toml          
└── docs/                    
    ├── detailed_doc.md      
    └── detailed_doc.docx

## Security & Best Practices

- **Environment Variables:**  
  Your `.env` file is listed in `.gitignore` so it is not tracked by Git. This keeps your sensitive Groq API key secure.
  
- **Avoid Hardcoding Secrets:**  
  Never include secrets directly in your code. Always use environment variables for sensitive data.

## Contributing

Contributions are welcome! Feel free to open issues or submit pull requests. For major changes, please open an issue first to discuss what you would like to change.

## License

This project is licensed under the [MIT License](LICENSE).

## Acknowledgments

- [LangChain](https://github.com/hwchase17/langchain) for providing a flexible framework for building language model apps.
- [Groq API](https://groq.com/) for LLM acceleration.
- The Streamlit community for an easy and interactive way to build web apps.



