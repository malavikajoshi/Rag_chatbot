# 🤖 Agentic RAG Chatbot for Multi-Format Document QA using MCP

This chatbot uses agent-based architecture to answer questions from uploaded documents (PDF, PPTX, DOCX, CSV, TXT) using a Retrieval-Augmented Generation (RAG) pipeline and Model Context Protocol (MCP).

## 💡 Features
- Upload multiple file types
- Ask contextual questions
- See source content for transparency
- Uses OpenAI's GPT-3.5 for answer generation

## 🚀 Tech Stack
- Python, Streamlit
- FAISS, Sentence Transformers
- OpenAI API
- PyPDF2, python-docx, pptx, pandas

## ⚙️ How to Run
```bash
git clone https://github.com/your-username/rag-chatbot.git
cd rag-chatbot
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate
pip install -r requirements.txt
streamlit run app.py

client = openai.OpenAI(api_key="your_openai_key")
