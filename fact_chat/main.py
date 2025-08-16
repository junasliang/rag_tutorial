from langchain.document_loaders import TextLoader
from langchain.text_splitter import CharacterTextSplitter
from dotenv import load_dotenv

if __name__ == "__main__":
    # load api key
    load_dotenv()

    # Seperate text to chunk
    text_splitter = CharacterTextSplitter(
        separator="\n",
        chunk_size=200,
        chunk_overlap=0,
    )

    # load fact txt
    loader = TextLoader("facts.txt")
    docs = loader.load_and_split(
        text_splitter=text_splitter
    )

    for doc in docs:
        print(doc.page_content)
        print('\n')