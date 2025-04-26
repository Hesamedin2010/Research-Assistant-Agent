from dotenv import load_dotenv
# Load environment variables from a .env file
load_dotenv()

from variables import llm
from langchain_core.runnables import RunnableSequence
from langchain_core.prompts import ChatPromptTemplate


# Define the planner prompt
planner_template = """
You are a research planning assistant.

Given a research query, your job is to break it down into a list of researchable sub-topics or steps. 
Each step should be specific, logical, and build toward answering the main question.

## Research Query:
{query}

## Instructions:
- Think step by step.
- Cover all aspects of the query up to 5 sub-topics.
- Do NOT answer the questions — just break them into parts.
- write all the sub-topics and separate them with commas

## Plan:
"""

planner_prompt = ChatPromptTemplate.from_messages(
    [
        ("system", planner_template),
        ("human", "query: \n\n {query}")
    ]
)

planner_chain: RunnableSequence = planner_prompt | llm