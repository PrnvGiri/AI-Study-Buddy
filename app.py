import os
import streamlit as st
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

from langchain_community.document_loaders import PyPDFLoader, TextLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_chroma import Chroma
from langchain_groq import ChatGroq
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnablePassthrough

# Page Configuration
st.set_page_config(page_title="AI Study Buddy", page_icon="📚", layout="centered")

st.title("📚 AI Study Buddy - Ray Optics 🎓")
st.caption("Powered by LangChain, Chroma DB & Groq (LLaMA 3.3)")


# Cache RAG setup so document is processed only once on app startup
@st.cache_resource
def init_rag_chain(filepath="RayOptics.pdf"):
    if filepath.endswith(".pdf"):
        loader = PyPDFLoader(filepath)
    else:
        loader = TextLoader(filepath)

    docs = loader.load()
    text_splitter = RecursiveCharacterTextSplitter(chunk_size=500, chunk_overlap=50)
    splits = text_splitter.split_documents(docs)

    embeddings = HuggingFaceEmbeddings(model_name="all-MiniLM-L6-v2")
    vectorstore = Chroma.from_documents(documents=splits, embedding=embeddings)
    retriever = vectorstore.as_retriever()

    llm = ChatGroq(model_name="llama-3.3-70b-versatile", temperature=1)

    template = """Answer the question based only on the following context: {context}

Question: {question}

Helpful Answer:"""

    prompt = ChatPromptTemplate.from_template(template)

    def format_docs(docs):
        return "\n\n".join(doc.page_content for doc in docs)

    chain = (
        {"context": retriever | format_docs, "question": RunnablePassthrough()}
        | prompt
        | llm
        | StrOutputParser()
    )

    return chain


# Initialize RAG Chain
rag_chain = init_rag_chain()

# Initialize Chat History in Session State
if "messages" not in st.session_state:
    st.session_state.messages = [
        {"role": "assistant", "content": "Hello! Ask me any question related to the Ray Optics document!"}
    ]

# Display Chat History
for msg in st.session_state.messages:
    st.chat_message(msg["role"]).write(msg["content"])

# User Question Input
if prompt := st.chat_input("Ask a question about Ray Optics..."):
    # Store and display user message
    st.session_state.messages.append({"role": "user", "content": prompt})
    st.chat_message("user").write(prompt)

    # Generate and display AI Study Buddy response
    with st.chat_message("assistant"):
        with st.spinner("Thinking..."):
            answer = rag_chain.invoke(prompt)
            st.write(answer)
            st.session_state.messages.append({"role": "assistant", "content": answer})
