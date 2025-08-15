# Most of the models are completion model
# How to maintain chat model
from langchain_openai import ChatOpenAI
from langchain.chains import LLMChain
from langchain.prompts import HumanMessagePromptTemplate, ChatPromptTemplate, MessagesPlaceholder

from langchain.memory import ConversationBufferMemory, ConversationSummaryBufferMemory, FileChatMessageHistory

from dotenv import load_dotenv

if __name__ == "__main__":
    load_dotenv()

    # set up chat
    chat = ChatOpenAI(verbose=True)
    # set up memory
    memory = ConversationSummaryBufferMemory(
        # chat_memory=FileChatMessageHistory("messages.json"),
        memory_key = "messages",
        return_messages = True,   # return object instead of text
        llm=chat,
    )
    
    prompt = ChatPromptTemplate(
        input_variables = ["content", "messages"],
        messages=[
            MessagesPlaceholder(variable_name="messages"),
            HumanMessagePromptTemplate.from_template("{content}")
        ]
    )

    chain = LLMChain(
        llm = chat,
        prompt = prompt,
        memory = memory,
        verbose = True,
    )

    while True:
        content = input(">>")
        result = chain({"content": content})

        print(result["text"])