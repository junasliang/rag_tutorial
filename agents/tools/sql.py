import sqlite3
from langchain.tools import Tool

# connect to sql database
conn = sqlite3.connect("db.sqlite")

# operation of sql database
def run_sqlite_query(query):
    c = conn.cursor()
    c.execute(query)
    return c.fetchall()

# create langchain tool
run_query_tool = Tool.from_function(
    name="run_squlite_query",
    description="Run a sqlite query.",
    func=run_sqlite_query,
)