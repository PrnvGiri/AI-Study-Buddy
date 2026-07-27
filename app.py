import os
from flask import Flask, render_template, request, jsonify
from dotenv import load_dotenv

load_dotenv()

from langchain_community.document_loaders import PyPDFLoader, TextLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_google_genai import GoogleGenerativeAIEmbeddings
from langchain_chroma import Chroma
from langchain_groq import ChatGroq
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnablePassthrough

app = Flask(__name__)


def load_and_split(filepath):
    if filepath.endswith(".pdf"):
        loader = PyPDFLoader(filepath)
    else:
        loader = TextLoader(filepath)

    docs = loader.load()
    splitter = RecursiveCharacterTextSplitter(chunk_size=2000, chunk_overlap=200)
    splits = splitter.split_documents(docs)
    return splits


def create_rag_chain(splits, db_dir="./chroma_db"):
    embeddings = GoogleGenerativeAIEmbeddings(
        model="models/gemini-embedding-001",
        task_type="RETRIEVAL_DOCUMENT"
    )

    # Reuse existing Chroma DB from disk if available to prevent hitting 429 API quota limits
    if os.path.exists(db_dir) and len(os.listdir(db_dir)) > 0:
        print("💾 Loading existing Chroma DB from disk (0 API quota used)...")
        vectorstore = Chroma(
            persist_directory=db_dir,
            embedding_function=embeddings
        )
    else:
        print("⚡ Creating new Chroma DB vector store...")
        vectorstore = Chroma.from_documents(
            documents=splits,
            embedding=embeddings,
            persist_directory=db_dir
        )

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


# Load RayOptics.pdf and build RAG Chain on server startup
print("⏳ Initializing AI Study Buddy vector store...")
splits = load_and_split("RayOptics.pdf")
rag_chain = create_rag_chain(splits)
print("✅ Study Buddy Web App is Ready!")


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/ask", methods=["POST"])
def ask():
    user_data = request.get_json()
    user_question = user_data.get("question", "")
    answer = rag_chain.invoke(user_question)
    return jsonify({"answer": answer})


if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5001))
    app.run(host="0.0.0.0", port=port)
