from sentence_transformers import SentenceTransformer
import faiss

model = SentenceTransformer('all-MiniLM-L6-v2')
index = faiss.IndexFlatL2(384)
texts = []

def embed_and_store(chunks):
    global texts
    embeddings = model.encode(chunks)
    index.add(embeddings)
    texts.extend(chunks)

def retrieve(query, k=3):
    q_vec = model.encode([query])
    D, I = index.search(q_vec, k)
    return [texts[i] for i in I[0]]
