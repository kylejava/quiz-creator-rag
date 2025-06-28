# RAG Quiz Creator

A Retrieval-Augmented Generation (RAG) system for creating quizzes from documents.

## Project Structure

```
quiz-creator-rag/
├── app/
│   └── main.py          # Streamlit application
├── requirements.txt     # Python dependencies
├── venv/               # Virtual environment
└── README.md           # This file
```

## Setup

1. **Activate Virtual Environment**
   ```bash
   venv\Scripts\activate.bat
   ```

2. **Install Dependencies**
   ```bash
   pip install streamlit
   ```

3. **Run the Application**
   ```bash
   streamlit run app/main.py
   ```

## Features

- Simple Streamlit interface
- Query input and response placeholder
- Ready for RAG implementation

## Next Steps

- [ ] Document loading functionality
- [ ] Vector database integration
- [ ] Embedding generation
- [ ] RAG pipeline implementation
- [ ] Quiz generation features 