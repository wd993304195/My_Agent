
import os
from langchain_community.document_loaders import PyPDFLoader, TextLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_community.vectorstores import FAISS
from langchain_community.embeddings import FastEmbedEmbeddings

DB_PATH = "data/faiss_index"

def load_docs(path):
    if path.endswith(".pdf"):
        return PyPDFLoader(path).load()
    return TextLoader(path, encoding="utf-8").load()

def get_embeddings():
    # FastEmbed: 轻量级本地 embedding，首次使用自动下载模型
    return FastEmbedEmbeddings(model_name="BAAI/bge-small-zh-v1.5")

def build_vectorstore(path):
    docs = load_docs(path)
    splitter = RecursiveCharacterTextSplitter(chunk_size=800, chunk_overlap=100)
    chunks = splitter.split_documents(docs)

    embeddings = get_embeddings()
    db = FAISS.from_documents(chunks, embeddings)
    db.save_local(DB_PATH)

def query_vectorstore(query):
    if not os.path.exists(DB_PATH):
        return ""
    embeddings = get_embeddings()
    db = FAISS.load_local(DB_PATH, embeddings, allow_dangerous_deserialization=True)
    docs = db.similarity_search(query, k=4)
    return "\n\n".join([d.page_content for d in docs])
