from utils import extract_text_from_file
from embeddings import embed_and_store
from mcp import create_mcp_message
import uuid

def process_files(files):
    all_text = []
    for file in files:
        content = extract_text_from_file(file)
        chunks = content.split('\n\n')[:10]  # naive chunking
        all_text.extend(chunks)
    embed_and_store(all_text)
    return create_mcp_message("IngestionAgent", "RetrievalAgent", "INGEST_COMPLETE", str(uuid.uuid4()), {"chunks": all_text})
