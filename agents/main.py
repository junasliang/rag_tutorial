from dotenv import load_dotenv
from langchain.agents import AgentExecutor, OpenAIFunctionsAgent
from langchain.memory import ConversationBufferMemory
from langchain.prompts import (
    ChatPromptTemplate,
    HumanMessagePromptTemplate,
    MessagesPlaceholder,
)
from langchain.schema import SystemMessage
from langchain_openai import ChatOpenAI
from tools.sql import describe_tables_tool, list_tables, run_query_tool

load_dotenv()

chat = ChatOpenAI()

tables = list_tables()

prompt = ChatPromptTemplate(
    messages=[
        SystemMessage(
            content=(
                "You are an AI that has access to a SQLite database.\n"
                f"The databse has tables of: {tables}\n"
                "Do not make any assumptions about what tables exist "
                "or what columns exist. Instead, use the 'describe_tables' function."
            )
        ),
        MessagesPlaceholder(variable_name="chat_history"),
        HumanMessagePromptTemplate.from_template("{input}"),
        MessagesPlaceholder(
            variable_name="agent_scratchpad"
        ),  # simplified form of memory
    ]
)

memory = ConversationBufferMemory(memory_key="chat_history", return_messages=True)

# define tools
tools = [run_query_tool, describe_tables_tool, describe_tables_tool]

# define agent
# (chain that uses tools)
agent = OpenAIFunctionsAgent(
    llm=chat,
    prompt=prompt,
    tools=tools,
)

# define agent executer
# (take agent and run until stop, fancy while loop)
agent_executor = AgentExecutor(
    agent=agent,
    verbose=True,
    tools=tools,
    memory=memory,
)

agent_executor(
    "Summarize the top 5 most popular products. Write the results to a report file."
)
# agent_executor("How many users are in the database?")

agent_executor("Repeat the exact same process for users.")
