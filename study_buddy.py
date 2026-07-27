import os
from dotenv import load_dotenv

load_dotenv()

from langchain_community.document_loaders import TextLoader, PyPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_google_genai import GoogleGenerativeAIEmbeddings
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

    print("Splitting Data into Chunks...")
    splitter = RecursiveCharacterTextSplitter(chunk_size=500, chunk_overlap=50)
    splits = splitter.split_documents(docs)
    print(f"Split {len(splits)} Chunks")
    return splits


def create_rag_chain(splits):
    # Free Cloud API Embeddings (Zero PyTorch overhead, ultra low memory)
    embeddings = GoogleGenerativeAIEmbeddings(model="models/text-embedding-004")
    vectorstore = Chroma.from_documents(documents=splits, embedding=embeddings)
    retriever = vectorstore.as_retriever()

    # LLM using Groq
    llm = ChatGroq(model_name="llama-3.3-70b-versatile", temperature=1)

    template = """Answer the question based only on the following context: {context}

Question: {question}

Helpful Answer:"""

    prompt = ChatPromptTemplate.from_template(template)

    def format_docs(docs):
        return "\n\n".join(doc.page_content for doc in docs)

    # RAG Chain
    chain = (
        {"context": retriever | format_docs, "question": RunnablePassthrough()}
        | prompt
        | llm
        | StrOutputParser()
    )

    return chain


# Load RayOptics.pdf, split chunks, build chain, and ask question
file_path = "RayOptics.pdf"

splits = load_and_split(file_path)
rag_chain = create_rag_chain(splits)

message = input("Ask a Question related to Ray Optics: ")
output = rag_chain.invoke(message)
print(output)
