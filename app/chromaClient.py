import chromadb
from ingest_data.document_loader import load_pdf_file
from ingest_data.text_splitter import split_text
from langchain.schema import Document
from ingest_data.embeddings import get_embeddings
from langchain_community.vectorstores import Chroma
from langchain_mistralai import MistralAIEmbeddings, ChatMistralAI
from langchain.chains import LLMChain
from dotenv import load_dotenv
from pydantic import SecretStr
import os
from prompt_templates.prompt import prompt_template
from langchain.prompts import PromptTemplate


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


    def get_documents(self):
        # Get total count of docs
        total_docs = self.client._collection.count()
        
        # Retrieve all documents by setting limit to total_docs
        result = self.client.get(include=["documents", "metadatas"], limit=total_docs)
        documents = result.get("documents", [])
        return documents



    def summarize_db(self):
        print("DB Summary:")
    
        count = self.client._collection.count()
        print(f"Total documents: {count}")

        # Embedding dimensions
        result = self.client.get(include=["embeddings", "metadatas"], limit=1)
        if result["embeddings"]:
            dim = len(result["embeddings"][0])
            print(f"📐 Embedding Dimensions: {dim}")

        # Metadata fields
        all_metadata = self.client.get(include=["metadatas"], limit=5)["metadatas"]
        keys = set()
        for metadata in all_metadata:
            if metadata:
                keys.update(metadata.keys())

    def create_quiz(self, query):
        print(f"Creating quiz for query: {query}")
        prompt = PromptTemplate(
            template=prompt_template,
            input_variables=["query", "text_excerpt"]
        )
        docs = self.get_documents()
        combined_text = "\n\n".join(docs)
        prompt_value = prompt.format(query=query, text_excerpt=combined_text)
        
        # Try different models in case of rate limits
        models_to_try = ["mistral-small-latest", "mistral-tiny", "open-mistral-7b"]
        
        for model_name in models_to_try:
            try:
                print(f"Trying model: {model_name}")
                llm = ChatMistralAI(model_name=model_name, temperature=0)
                chain = LLMChain(llm=llm, prompt=prompt)
                response = chain.invoke({"query": query, "text_excerpt": combined_text})
                return response['text']
            except Exception as e:
                print(f"Error with model {model_name}: {str(e)}")
                if "429" in str(e) or "capacity exceeded" in str(e).lower():
                    print(f"Rate limit hit for {model_name}, trying next model...")
                    continue
                else:
                    raise e
        
        # If all models fail, return an error message
        raise Exception("All Mistral models are currently at capacity. Please try again later.")