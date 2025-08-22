# Most of the models are completion model
# How to maintain chat model
from dotenv import load_dotenv
from langchain.chains import LLMChain
from langchain.memory import (
    ConversationSummaryBufferMemory,
)
from langchain.prompts import (
    ChatPromptTemplate,
    HumanMessagePromptTemplate,
    MessagesPlaceholder,
)
from langchain_openai import ChatOpenAI

if __name__ == "__main__":
    load_dotenv()

    # set up chat
    chat = ChatOpenAI(verbose=True)
    # set up memory
    memory = ConversationSummaryBufferMemory(
        # chat_memory=FileChatMessageHistory("messages.json"),
        memory_key="messages",
        return_messages=True,  # return object instead of text
        llm=chat,
    )

    prompt = ChatPromptTemplate(
        input_variables=["content", "messages"],
        messages=[
            MessagesPlaceholder(variable_name="messages"),
            HumanMessagePromptTemplate.from_template("{content}"),
        ],
    )

    chain = LLMChain(
        llm=chat,
        prompt=prompt,
        memory=memory,
        verbose=True,
    )

    while True:
        content = input(">>")
        result = chain({"content": content})

        print(result["text"])
