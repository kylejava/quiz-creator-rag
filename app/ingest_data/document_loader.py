from langchain_community.document_loaders import PyMuPDFLoader
from pprint import pprint
import os
import sys

pdf_file_path = "../../document/book.pdf"

def load_pdf_file(pdf_file_path):
    loader_py = PyMuPDFLoader(pdf_file_path)
    docs = loader_py.load()
    for doc in docs:
        doc.metadata["source"] = pdf_file_path
        doc.metadata["file_type"] = "pdf"
    
    return docs


