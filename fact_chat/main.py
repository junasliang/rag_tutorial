from langchain.document_loaders import TextLoader
from langchain.text_splitter import CharacterTextSplitter
from langchain_openai import OpenAIEmbeddings
from langchain.vectorstores.chroma import Chroma
from dotenv import load_dotenv

if __name__ == "__main__":
    # load api key
    load_dotenv()

    # embeddings
    embeddings = OpenAIEmbeddings()
    emb = embeddings.embed_query("hi there")

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

    # reaching openai tokens
    # every single time you run, you duplicate once
    db = Chroma.from_documents(
        docs,
        embedding=embeddings,
        persist_directory="emb",
    )

    results = db.similarity_search_with_score(
        "What is an interesting fact about english language?",
        k=2,
        )

    for result in results:
        print("\n")
        print(result[1])
        print(result[0].page_content)