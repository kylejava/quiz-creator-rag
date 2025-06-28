from langchain_text_splitters import RecursiveCharacterTextSplitter


def split_text(text):
    text_splitter = RecursiveCharacterTextSplitter(
        chunk_size=1000,
        chunk_overlap=200,
        length_function=len,
        #separators=["\n\n", "\n", ". ", "! ", "? ", " ", ""]

    )
    return text_splitter.split_text(text)