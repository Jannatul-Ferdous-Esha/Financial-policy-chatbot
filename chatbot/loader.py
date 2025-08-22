from PyPDF2 import PdfReader
from langchain.text_splitter import RecursiveCharacterTextSplitter

def load_policy_document(pdf_path: str):
    reader = PdfReader(pdf_path)
    documents = []
    for i, page in enumerate(reader.pages):
        text = page.extract_text()
        if text and text.strip():
            documents.append({"text": text, "metadata": {"page": i + 1}})
    return documents

def check_pdf_extraction(pdf_path: str):
    reader = PdfReader(pdf_path)
    documents = []
    for i, page in enumerate(reader.pages):
        text = page.extract_text()
        if text and text.strip():
            print(f"Page {i+1}: {len(text)} characters")
            if len(text) > 200:
                print(f"First 200 chars: {text[:200]}...")
            else:
                print(f"Content: {text}")
            documents.append({"text": text, "metadata": {"page": i + 1}})
        else:
            print(f"Page {i+1}: No text extracted")
    return documents

def chunk_documents(docs, chunk_size=500, overlap=100):
    splitter = RecursiveCharacterTextSplitter(chunk_size=chunk_size, chunk_overlap=overlap)
    texts = [d["text"] for d in docs]
    metadatas = [d["metadata"] for d in docs]
    chunks = splitter.create_documents(texts, metadatas=metadatas)
    return chunks