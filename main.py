
import os
from dotenv import load_dotenv
from chatbot.loader import load_policy_document, chunk_documents, check_pdf_extraction
from chatbot.vectorstore import build_vectorstore, load_vectorstore
from chatbot.bot import build_chatbot, ask_chatbot

PDF_PATH = "data/For Task - Policy file.pdf"
DB_PATH = "db/chroma"

def setup():
    
    if not os.path.exists(DB_PATH) or not os.listdir(DB_PATH):
        print(" Extracting and indexing financial policy...")
        
        
        print("Checking PDF extraction...")
        docs = check_pdf_extraction(PDF_PATH)
        
        if not docs or all(not doc['text'].strip() for doc in docs):
            print(" No text could be extracted from the PDF.")
            print("The PDF might be scanned or image-based. Please provide a text-based PDF.")
            return None
        
        chunks = chunk_documents(docs)
        print(f"Created {len(chunks)} chunks from the document")
        
        vectordb = build_vectorstore(chunks, persist_directory=DB_PATH)
        print(" Vector database created successfully!")
    else:
        print(" Using existing vector database...")
        vectordb = load_vectorstore(persist_directory=DB_PATH)
    
    
    test_retriever = vectordb.as_retriever(search_kwargs={"k": 4})
    
    
    test_queries = ["budget", "financial", "policy", "government", "taxation", "GSP"]
    for query in test_queries:
        test_docs = test_retriever.invoke(query)
        print(f"Found {len(test_docs)} documents for query: '{query}'")
        if test_docs:
            print(f"First document content: {test_docs[0].page_content[:200]}...")
    
    return vectordb

if __name__ == "__main__":
    load_dotenv()  
    vectordb = setup()
    
    if vectordb is None:
        print(" Failed to set up the vector database. Exiting.")
        exit(1)
    
   
    qa_chain = build_chatbot(vectordb)

    print("\n Financial Policy Chatbot Ready! Type 'exit' to quit.\n")
    while True:
        query = input("You: ")
        if query.lower() in ["exit", "quit"]:
            print("Chatbot: Goodbye!")
            break
        
        response = ask_chatbot(qa_chain, query)
        print("Chatbot:", response, "\n")