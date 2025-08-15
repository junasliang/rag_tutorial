# old api version
from langchain_community.llms import OpenAI
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain, SequentialChain

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

    code_prompt = PromptTemplate(
        input_variables=["language", "task"],
        template="Write a very short {language} function that will {task}",
    )

    test_promt = PromptTemplate(
        input_variables=["language", "task"],
        template="Write a test for the following {language} code:\n{code}"
    )

    code_chain = LLMChain(
        llm = llm,
        prompt = code_prompt,
        output_key = "code" 
    )

    test_chain = LLMChain(
        llm = llm,
        prompt = test_promt,
        output_key = "test"
    )

    chain = SequentialChain(
        chains = [code_chain, test_chain],
        input_variables = ["task", "language"],
        output_variables = ["test", "code"]
    )

    res = chain({
        "language": args.language,
        "task": args.task
    })
    print(res["code"])
    print(res["test"])