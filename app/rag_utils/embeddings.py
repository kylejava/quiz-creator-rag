import os
import getpass
from langchain_mistralai import MistralAIEmbeddings

if not os.getenv("MISTRALAI_API_KEY"):
    os.environ["MISTRALAI_API_KEY"] = getpass.getpass("Enter your MistralAI API key: ")

def get_embeddings(docs):
    embeddings = MistralAIEmbeddings(
        model="mistral-embed",
        api_key=os.getenv("MISTRALAI_API_KEY"),
    )
    return embeddings.embed_documents(docs)