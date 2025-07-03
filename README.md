# RAG Quiz Creator

A Retrieval-Augmented Generation (RAG) system for creating quizzes from documents using Mistral AI and ChromaDB.

## Project Structure

```
quiz-creator-rag/
├── app/
│   ├── main.py                    # Streamlit web application
│   ├── chromaClient.py            # ChromaDB client and RAG implementation
│   ├── test.py                    # RAG pipeline testing script
│   ├── chroma_db/                 # ChromaDB vector database storage
│   ├── ingest_data/
│   │   ├── document_loader.py     # PDF document loading functionality
│   │   ├── text_splitter.py       # Text chunking and splitting
│   │   └── embeddings.py          # Mistral AI embeddings generation
│   └── prompt_templates/
│       └── prompt.py              # Quiz generation prompt template
├── document/                      # Document storage directory
├── requirements.txt               # Python dependencies
├── venv/                         # Virtual environment
├── .gitignore                    # Git ignore rules
└── README.md                     # This file
```

## Features

✅ **Implemented Features:**
- PDF document loading and processing
- Text chunking with RecursiveCharacterTextSplitter
- Mistral AI embeddings generation
- ChromaDB vector database integration
- RAG-based quiz generation using Mistral AI
- Streamlit web interface with:
  - Query input for quiz generation
  - Database summary popup dialog
  - Loading spinners and error handling
  - Formatted quiz output display

## Setup

1. **Clone the Repository**
   ```bash
   git clone <repository-url>
   cd quiz-creator-rag
   ```

2. **Activate Virtual Environment**
   ```bash
   venv\Scripts\activate
   ```

3. **Install Dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Environment Variables**
   Create a `.env` file in the root directory with:
   ```
   MISTRAL_API_KEY=your_mistral_api_key_here
   ```

5. **Add Documents**
   Place your PDF documents in the `document/` directory

6. **Run the Application**
   ```bash
   streamlit run app/main.py
   ```

## Dependencies

- **streamlit==1.28.1** - Web application framework
- **langchain==0.0.350** - LLM framework
- **langchain-community==0.0.10** - Community integrations
- **chromadb==0.4.18** - Vector database
- **sentence-transformers==2.2.2** - Text embeddings
- **python-dotenv==1.0.0** - Environment variable management
- **pypdf==3.17.1** - PDF processing
- **docx2txt==0.8** - Document text extraction

## Usage

1. **Start the Application**: Run `streamlit run app/main.py`
2. **Enter a Query**: Type your question in the text input
3. **Generate Quiz**: Click "Get Response" to create a quiz
4. **View Database**: Click "Show Database Summary" to see stored documents

## Technical Details

- **Vector Database**: ChromaDB with persistent storage
- **Embeddings**: Mistral AI embeddings (mistral-embed model)
- **LLM**: Mistral AI chat models with fallback support
- **Text Processing**: Recursive character text splitting with 1000 character chunks
- **Error Handling**: Automatic model fallback for rate limits

## Next Steps

- [ ] Add support for more document formats (DOCX, TXT)
- [ ] Implement quiz export functionality
- [ ] Add quiz difficulty levels
- [ ] Implement user authentication
- [ ] Add quiz history and saving
- [ ] Optimize for larger documents 