import streamlit as st
from agents.ingestion_agent import process_files
from agents.retrieval_agent import retrieve_relevant_context
from agents.llm_response_agent import generate_response

st.title("📄 Agentic RAG Chatbot")

uploaded_files = st.file_uploader("Upload documents", type=["pdf", "pptx", "csv", "docx", "txt", "md"], accept_multiple_files=True)
query = st.text_input("Ask a question")

if uploaded_files:
    mcp_ingest = process_files(uploaded_files)
    st.success("Ingestion complete")

if st.button("Get Answer"):
    if query:
        mcp_retrieve = retrieve_relevant_context(query)
        answer = generate_response(mcp_retrieve)
        st.markdown(f"**Answer:** {answer}")
        with st.expander("Source Chunks"):
            st.write("\n\n".join(mcp_retrieve["payload"]["retrieved_context"]))
