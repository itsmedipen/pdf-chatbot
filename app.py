import os# access my api key
import streamlit as st
from dotenv import load_dotenv #load api environment
from PyPDF2 import PdfReader# #get pdf text
from langchain_community.document_loaders import PyPDFLoader
from langchain.text_splitter import CharacterTextSplitter
from langchain_community.vectorstores import FAISS
from langchain.embeddings import HuggingFaceEmbeddings
from langchain.chains.question_answering import load_qa_chain
from langchain_groq import ChatGroq
from langchain.chains import RetrievalQA

#setting the api key environment and load the api key in environment
def main():
    load_dotenv()
    # print(os.getenv('GROQ_API_KEY'))#checking api key is loading or not
    groq_api_key = os.getenv('GROQ_API_KEY')

    
    #setting gpu

    st.set_page_config(page_title='Chat with pdf',page_icon='books')# title of the page
    
    st.header('PDF Chatbot :books:')# header of the page
    # st.text_input('Ask a question about your documents')

    with st.sidebar:#create a sidebar
        st.subheader('Upload a PDF file and click "Process" to start chat.')# create a header inside sidebar
        #uploading the file
        # st.write('Upload a PDF file and click "Process" to start chatting with your document.')
        pdf = st.file_uploader('',type='pdf')#create a file uploader
        # when clicking button
        if st.button('Process',"Primary Button", type="primary"):#create button
            with st.spinner('processing..'):#create spinner
                #logic part
                #step:1
                #get text out of the pdf
                if pdf is not None:# pdf is not null
                    pdf_reader = PdfReader(pdf) # create a object pdf_reader of PdfReader
                    text = ''
                    for page in pdf_reader.pages:
                        text += page.extract_text()
                        #split into chunks
                        text_splitter = CharacterTextSplitter(separator='\n',chunk_size=1000, chunk_overlap=200,length_function = len)
                        #seperator = new line which separate the chunks, chunk_size = first 1000 characters and so on
                        #chunk_overlap = repeate the 200 characters in every chunks
                        #length_function = length of chunks
                        docs = text_splitter.split_text(text)#split text

                        # st.write(docs)

                        # Embed documents
                        embeddings = HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2")
                        vectorstore = FAISS.from_texts(docs, embeddings)

                        llm = ChatGroq(groq_api_key=groq_api_key, model_name="openai/gpt-oss-120b")
                        st.session_state.qa_chain = RetrievalQA.from_chain_type(llm=llm, retriever=vectorstore.as_retriever())
                        
                    st.success('Completed')
                    
    if "qa_chain" in st.session_state:
        user_question = st.text_input("Ask a question from the PDF:")
        if user_question:
            response = st.session_state.qa_chain.run(user_question)
            st.write("### 🧠🤖 Answer:")
            st.write(response)
                #get text chunks
                #create our vector stores
                

if __name__ == '__main__':
    main()

st.markdown(
    """
    <style>
    .footer {
        position: fixed;
        bottom: 10px;
        left: 0;
        width: 100%;
        text-align: center;
        font-size: 0.9em;
        color: gray;
    }
    </style>
    <div class="footer">
        🧑Developed by <strong>Dipen Sherpa</strong>&nbsp;|&nbsp; © 2025
    </div>
    """,
    unsafe_allow_html=True
)



