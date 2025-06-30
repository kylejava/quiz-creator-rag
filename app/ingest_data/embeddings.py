import os
from langchain_mistralai import MistralAIEmbeddings
from dotenv import find_dotenv, load_dotenv
from pydantic import SecretStr

dotenv_path = find_dotenv()
load_dotenv(dotenv_path)

key = os.getenv("MISTRAL_API_KEY")

#May Not Be Needed

def get_embeddings():
    
    return MistralAIEmbeddings(
        model="mistral-embed",
        api_key=SecretStr(key)
    )
