from embeddings import retrieve
from mcp import create_mcp_message
import uuid

def retrieve_relevant_context(query):
    chunks = retrieve(query)
    return create_mcp_message("RetrievalAgent", "LLMResponseAgent", "RETRIEVAL_RESULT", str(uuid.uuid4()), {
        "retrieved_context": chunks,
        "query": query
    })
