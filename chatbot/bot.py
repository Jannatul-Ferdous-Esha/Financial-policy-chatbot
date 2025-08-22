
from langchain.chains import RetrievalQA
from langchain.prompts import PromptTemplate
from langchain_community.llms import FakeListLLM

def build_chatbot(vectordb):
    
    responses = ["I'll provide information based on the document content."]
    llm = FakeListLLM(responses=responses)

    
    retriever = vectordb.as_retriever(search_kwargs={"k": 6})
    
    
    qa_chain = RetrievalQA.from_chain_type(
        llm=llm,
        chain_type="stuff",
        retriever=retriever,
        return_source_documents=True
    )

    return qa_chain

def ask_chatbot(qa_chain, query: str):
    try:
        
        result = qa_chain.invoke({"query": query})
        
        
        if "source_documents" in result and result["source_documents"]:
            
            answer_parts = []
            for i, doc in enumerate(result["source_documents"]):
                answer_parts.append(f"Relevant information {i+1}: {doc.page_content[:300]}...")
            
            answer = "\n\n".join(answer_parts)
            
            
            pages = {doc.metadata.get("page") for doc in result["source_documents"]}
            if pages:
                answer += f"\n\n (References: Pages {', '.join(map(str, sorted(pages)))})"
        else:
            answer = "I couldn't find relevant information in the document to answer your question. Please try rephrasing your query or ask about a different topic."
        
        return answer
    except Exception as e:
        return f"Sorry, I encountered an error while processing your query: {str(e)}"