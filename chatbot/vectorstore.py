

from langchain_huggingface import HuggingFaceEmbeddings
from langchain_chroma import Chroma

def build_vectorstore(chunks, persist_directory="db/chroma"):
    embeddings = HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2")
    vectordb = Chroma.from_documents(
        documents=chunks,
        embedding=embeddings,
        persist_directory=persist_directory
    )
    
    return vectordb

def load_vectorstore(persist_directory="db/chroma"):
    embeddings = HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2")
    vectordb = Chroma(
        persist_directory=persist_directory,
        embedding_function=embeddings
    )
    return vectordb