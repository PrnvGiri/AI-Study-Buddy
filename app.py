import os
import gradio as gr
from dotenv import load_dotenv

load_dotenv()

from langchain_community.document_loaders import PyPDFLoader, TextLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_chroma import Chroma
from langchain_groq import ChatGroq
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnablePassthrough


def load_and_split(filepath):
    if filepath.endswith(".pdf"):
        loader = PyPDFLoader(filepath)
    else:
        loader = TextLoader(filepath)

    docs = loader.load()
    splitter = RecursiveCharacterTextSplitter(chunk_size=500, chunk_overlap=50)
    splits = splitter.split_documents(docs)
    return splits


def create_rag_chain(splits):
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


# Load RayOptics.pdf and build RAG Chain
print("⏳ Initializing AI Study Buddy vector store...")
splits = load_and_split("RayOptics.pdf")
rag_chain = create_rag_chain(splits)
print("✅ Study Buddy Gradio App is Ready!")


def respond(message, history):
    return rag_chain.invoke(message)


demo = gr.ChatInterface(
    fn=respond,
    title="📚 AI Study Buddy - Ray Optics 🎓",
    description="Ask any question regarding the Ray Optics study material!",
    textbox=gr.Textbox(placeholder="Ask a question regarding Ray Optics...")
)

if __name__ == "__main__":
    demo.launch(share=True)
