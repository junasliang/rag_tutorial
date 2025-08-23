import sqlite3
from langchain.tools import Tool

# connect to sql database
conn = sqlite3.connect("db.sqlite")

# operation of sql database
def run_sqlite_query(query):
    c = conn.cursor()
    try:
        c.execute(query)
        return c.fetchall()
    except sqlite3.OperationalError as err:
        return f"The following error occrued: {str(err)}"
    
def list_tables():
    c = conn.cursor()
    c.execute("SELECT name FROM sqlite_master WHERE type='table';")
    rows = c.fetchall()
    return "\n".join(row[0] for row in rows if row[0] is not None)
    
# create langchain tool
run_query_tool = Tool.from_function(
    name="run_squlite_query",
    description="Run a sqlite query.",
    func=run_sqlite_query,
)

def describe_tables(tables_names):
    c = conn.cursor()
    tables = ','.join("'" + table + "'" for table in tables_names)
    rows = c.execute(f"SELECT sql FROM sqlite_master WHERE type='table' AND name IN ({tables});")
    return '\n'.join(row[0] for row in rows if row[0] is not None)

describe_tables_tool = Tool.from_function(
    name="describe_tables",
    description="Given a list of table names, returns the schema of those tables",
    func=describe_tables,
)
