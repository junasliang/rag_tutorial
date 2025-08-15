# old api version
from langchain_community.llms import OpenAI
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain

import argparse
from dotenv import load_dotenv

if __name__ == "__main__":
    # arg parsers
    parser = argparse.ArgumentParser()
    parser.add_argument("--task", default="return a list of numbers")
    parser.add_argument("--language", default="python")
    args = parser.parse_args()

    # load env
    load_dotenv()

    llm = OpenAI()

    code_promt = PromptTemplate(
        template="Write a very short {language} function that will {task}",
        input_variables=["language", "task"]   
    )

    code_chain = LLMChain(
        llm = llm,
        prompt = code_promt,
        output_key = "code" 
    )

    res = code_chain({
        "language": args.language,
        "task": args.task
    })
    print(res["code"])