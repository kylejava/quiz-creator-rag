import os
from langchain_mistralai import MistralAIEmbeddings
from dotenv import find_dotenv, load_dotenv
from pydantic import SecretStr

dotenv_path = find_dotenv()
load_dotenv(dotenv_path)

key = os.getenv("MISTRAL_API_KEY")


def get_embeddings(docs):
    
    embeddings = MistralAIEmbeddings(
        model="mistral-embed",
        api_key=SecretStr(key)
    )

    return embeddings.embed_documents(docs)