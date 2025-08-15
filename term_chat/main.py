# Most of the models are completion model
# How to maintain chat model
from langchain_openai import ChatOpenAI
from langchain.chains import LLMChain
from langchain.prompts import HumanMessagePromptTemplate, ChatPromptTemplate

from dotenv import load_dotenv

if __name__ == "__main__":
    load_dotenv()

    chat = ChatOpenAI()

    prompt = ChatPromptTemplate(
        input_variables = ["content"],
        messages=[
            HumanMessagePromptTemplate.from_template("{content}")
        ]
    )

    chain = LLMChain(
        llm = chat,
        prompt = prompt
    )

    while True:
        content = input(">>")
        result = chain({"content": content})

        print(result["text"])