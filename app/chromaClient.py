import chromadb
from ingest_data.document_loader import load_pdf_file
from ingest_data.text_splitter import split_text
from langchain.schema import Document
from ingest_data.embeddings import get_embeddings
from langchain_community.vectorstores import Chroma
from langchain_mistralai import MistralAIEmbeddings
from dotenv import load_dotenv
from pydantic import SecretStr
import os


class ChromaClient:
    def __init__(self, embeddings=None):
        self.db_directory = "./chroma_db"
        
        self.embeddings = embeddings if embeddings else get_embeddings()
        
        if os.path.exists(self.db_directory) and os.path.isdir(self.db_directory):
            self.client = Chroma(
                persist_directory=self.db_directory,
                embedding_function=self.embeddings
            )
            print("Collection already exists")
        else:
            documents = load_pdf_file("../document/diary-of-a-wimpy-kid-book-1-kinney-jeff.pdf")
            chunks = split_text(documents)
            
            docs_for_chroma = [Document(page_content=chunk, metadata={"source": "pdf"}) for chunk in chunks]
            
            self.client = Chroma.from_documents(
                documents=docs_for_chroma,
                embedding=self.embeddings,
                persist_directory=self.db_directory
            )
            self.client.persist()
            print("Collection created")


    def query_vector_store(self, query):
        pass

    