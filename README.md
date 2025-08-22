# 🏛️ Financial Policy Chatbot

The **Financial Policy Chatbot** is an AI-powered question-answering system designed to help users explore financial policy documents, budgetary statements, and government fiscal strategies.  
It leverages Natural Language Processing (NLP) and semantic search to provide **context-aware, reference-based responses** from financial documents.  

---

## 🚀 Features

- 📑 **Document Search**: Retrieves relevant information from financial policy documents.  
- 🤖 **Question-Answering**: Answers user queries with supporting references.  
- 📊 **Policy Insights**: Helps users understand government budgets, fiscal risks, taxation, and financial management strategies.  
- 🔍 **Vector Database**: Uses embeddings for efficient information retrieval.  

---

## ⚙️ Installation

1. Clone the repository:
   \`\`\`bash
   git clone https://github.com/Jannatul-Ferdous-Esha/Financial-policy-chatbot.git
   cd Financial-policy-chatbot
   \`\`\`

2. Create and activate a virtual environment:
   \`\`\`bash
   python -m venv venv
   source venv/bin/activate   # For Linux/Mac
   venv\Scripts\activate      # For Windows
   \`\`\`

3. Install dependencies:
   \`\`\`bash
   pip install -r requirements.txt
   \`\`\`

---

## ▶️ Usage

1. Run the chatbot:
   \`\`\`bash
   python main.py
   \`\`\`

2. Example interaction:
   \`\`\`
   Financial Policy Chatbot Ready! Type 'exit' to quit.

   You: Under which Act is the Territory’s Budget prepared?
   Chatbot: Relevant information 1: 
   The presentation and preparation of the Territory’s Budget is provided for in sections 11 and
   11A of the Financial Management Act 1996 (the Act).
   ...
   (References: Pages 1, 4, 5, 6)
   \`\`\`

   \`\`\`
   You: How does the Government manage fiscal risks to the Territory?
   Chatbot: Relevant information 1: 
   Achieving and maintaining levels of Territory net worth to provide a buffer against adverse factors...
   ...
   (References: Pages 1, 4, 5, 6)
   \`\`\`

3. To exit:
   \`\`\`
   exit
   \`\`\`

---

## 📂 Project Structure

\`\`\`
Financial-policy-chatbot/
│── data/               # Financial documents
│── chatbot/            # Core chatbot logic & vector store
│── main.py             # Entry point for running chatbot
│── requirements.txt    # Dependencies
│── README.md           # Project documentation
\`\`\`

---

## 🧠 How It Works

1. **Document Ingestion**: Loads financial policy documents into a vector database.  
2. **Embeddings**: Transforms text into embeddings for semantic similarity search.  
3. **Query Processing**: User questions are converted into vectors and matched against stored documents.  
4. **Answer Generation**: Retrieves top matches and presents summarized answers with references.  

---

## 📌 Example Queries

- *“Under which Act is the Territory’s Budget prepared?”*  
- *“How does the Government manage fiscal risks to the Territory?”*  
- *“What are the financial policy objectives of the Government?”*  
- *“Explain taxation strategy in the Territory.”*  

---

## 🛠️ Tech Stack

- **Python** 🐍  
- **LangChain** (for embeddings & retrieval)  
- **Vector Database** (e.g., FAISS/Chroma)  
- **OpenAI API** (for response generation)  

---

## 👩‍💻 Author

**Jannatul Ferdous Esha**  
📧 Contact: [GitHub Profile](https://github.com/Jannatul-Ferdous-Esha)  
