import streamlit as st

def main():
    st.title("RAG Quiz Creator")
    
    # Query input
    query = st.text_input("Enter your question:")
    
    # Submit button
    if st.button("Get Response"):
        if query:
            # Placeholder response
            st.write("**Response:** This is a placeholder response. RAG system not yet implemented.")
        else:
            st.warning("Please enter a question.")

if __name__ == "__main__":
    main() 