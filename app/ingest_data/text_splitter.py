from langchain_text_splitters import RecursiveCharacterTextSplitter


def split_text(docs):
    text_splitter = RecursiveCharacterTextSplitter(
        chunk_size=1000,
        chunk_overlap=200,
        length_function=len,
        #separators=["\n\n", "\n", ". ", "! ", "? ", " ", ""]

    )
    all_text = ""
    for doc in docs:
        all_text += doc.page_content + "\n\n"
    return text_splitter.split_text(all_text)