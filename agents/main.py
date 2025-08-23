from langchain_openai import ChatOpenAI
from langchain.prompts import(
    ChatPromptTemplate,
    HumanMessagePromptTemplate,
    MessagesPlaceholder,
)

from langchain.agents import OpenAIFunctionsAgent, AgentExecutor
from dotenv import load_dotenv

from tools.sql import run_query_tool


load_dotenv()

chat = ChatOpenAI()
prompt = ChatPromptTemplate(
    messages=[
        HumanMessagePromptTemplate.from_template("{input}"),
        MessagesPlaceholder(variable_name="agent_scratchpad") #simplified form of memory
    ]
)

# define tools
tools = [run_query_tool]

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
)

agent_executor("How many users are in the database?")