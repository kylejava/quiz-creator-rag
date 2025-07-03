import streamlit as st
from chromaClient import ChromaClient


def main():
    chroma_client = ChromaClient()
    st.title("RAG Quiz Creator")
    
    # Query input
    query = st.text_input("Enter your question:")
    
    # Submit button
    if st.button("Get Response"):
        if query:
            try:
                with st.spinner("Creating quiz..."):
                    ans = chroma_client.create_quiz(query)
                st.success("Quiz created successfully!")
                st.write("**Quiz Response:**")
                st.text_area("Generated Quiz", value=ans, height=400, disabled=True)
            except Exception as e:
                st.error(f"Error creating quiz: {str(e)}")
        else:
            st.warning("Please enter a question.")
    
    # Add separator
    st.divider()
    
    # Database summary button with popup dialog
    if st.button("Show Database Summary"):
        # Create a popup-like dialog using st.expander
        with st.expander("Database Summary", expanded=True):
            st.write("**Database Summary:**")
            # Capture the output from summarize_db
            import io
            import sys
            
            # Redirect stdout to capture print statements
            old_stdout = sys.stdout
            new_stdout = io.StringIO()
            sys.stdout = new_stdout
            
            try:
                chroma_client.summarize_db()
                output = new_stdout.getvalue()
                st.text(output)
            finally:
                sys.stdout = old_stdout

if __name__ == "__main__":
    main() 