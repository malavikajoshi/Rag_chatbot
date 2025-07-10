import openai
import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Read the API key
api_key = os.getenv("OPENAI_API_KEY")

# Ensure it's not None
if not api_key:
    raise ValueError("OpenAI API key not found. Please set OPENAI_API_KEY in your .env file or Streamlit secrets.")

# Pass the key to the client
client = openai.OpenAI(api_key=api_key)

def generate_response(mcp_msg):
    context = "\n".join(mcp_msg["payload"]["retrieved_context"])
    query = mcp_msg["payload"]["query"]

    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": f"Answer based on the context:\n{context}"},
            {"role": "user", "content": query}
        ]
    )

    return response.choices[0].message.content
