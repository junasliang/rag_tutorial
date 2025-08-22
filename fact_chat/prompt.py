from dotenv import load_dotenv
from langchain.chains import RetrievalQA
from langchain.chat_models import ChatOpenAI
from langchain.embeddings import OpenAIEmbeddings
from langchain.vectorstores import Chroma

load_dotenv()

chat = ChatOpenAI()
embeddings = OpenAIEmbeddings()
# create embeddings db
db = Chroma(persist_directory="emb", embedding_function=embeddings)

retriever = db.as_retriever()

chain = RetrievalQA.from_chain_type(llm=chat, retriever=retriever, chain_type="stuff")

result = chain.run("What is an interesting fact about English language?")

print(result)
