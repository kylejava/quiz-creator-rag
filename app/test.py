import sys
import os
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from ingest_data.document_loader import load_pdf_file
from ingest_data.text_splitter import split_text
from rag_utils.embeddings import get_embeddings

def test_rag_pipeline():
    print("🧪 Testing RAG Pipeline Step by Step")
    print("=" * 50)
    
    # Step 1: Document Loading
    print("\n📄 STEP 1: Document Loading")
    print("-" * 30)
    try:
        pdf_path = os.path.join(os.path.dirname(__file__), "..", "document", "diary-of-a-wimpy-kid-book-1-kinney-jeff.pdf")
        docs = load_pdf_file(pdf_path)
        print(f"✅ Documents loaded successfully!")
        print(f"📊 Type: {type(docs)}")
        print(f"📊 Number of documents: {len(docs)}")
        print(f"📊 First document type: {type(docs[0]) if docs else 'No docs'}")
        if docs:
            print(f"📊 First document content preview: {docs[0].page_content[:100]}...")
            print(f"📊 First document metadata: {docs[0].metadata}")
    except Exception as e:
        print(f"❌ Error loading documents: {e}")
        return
    
    # Step 2: Text Splitting
    print("\n✂️ STEP 2: Text Splitting")
    print("-" * 30)
    try:
        # Extract text content from all documents
        all_text = ""
        for doc in docs:
            all_text += doc.page_content + "\n\n"
        
        print(f"📊 Total text length: {len(all_text)} characters")
        chunks = split_text(all_text)
        print(f"✅ Text split successfully!")
        print(f"📊 Type: {type(chunks)}")
        print(f"📊 Number of chunks: {len(chunks)}")
        print(f"📊 First chunk type: {type(chunks[0]) if chunks else 'No chunks'}")
        if chunks:
            print(f"📊 First chunk preview: {chunks[0][:100]}...")
            print(f"📊 Average chunk length: {sum(len(chunk) for chunk in chunks) // len(chunks)} characters")
    except Exception as e:
        print(f"❌ Error splitting text: {e}")
        return
    
    # Step 3: Embeddings
    print("\n🔢 STEP 3: Embeddings")
    print("-" * 30)
    try:
        # Take first few chunks for testing (to save API calls)
        test_chunks = chunks[:3] if len(chunks) >= 3 else chunks
        embeddings = get_embeddings(test_chunks)
        print(f"✅ Embeddings generated successfully!")
        print(f"📊 Type: {type(embeddings)}")
        print(f"📊 Number of embeddings: {len(embeddings)}")
        print(f"📊 First embedding type: {type(embeddings[0]) if embeddings else 'No embeddings'}")
        if embeddings:
            print(f"📊 First embedding length: {len(embeddings[0])}")
            print(f"📊 First embedding preview: {embeddings[0][:5]}...")
    except Exception as e:
        print(f"❌ Error generating embeddings: {e}")
        return
    
    print("\n🎉 RAG Pipeline Test Complete!")
    print("=" * 50)

if __name__ == "__main__":
    test_rag_pipeline()
