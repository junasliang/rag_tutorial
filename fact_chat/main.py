from langchain.document_loaders import TextLoader
from dotenv import load_dotenv

if __name__ == "__main__":
    # load api key
    load_dotenv()

    # load fact txt
    loader = TextLoader("facts.txt")
    docs = loader.load()
    
    print(docs)