from dotenv import load_dotenv
# Load environment variables from a .env file
load_dotenv()

from variables import llm
from langchain_core.runnables import RunnableSequence
from langchain_core.prompts import ChatPromptTemplate


# Define the planner prompt
revisor_template = """
You are a research assistant tasked with verifying and revising research text.

You will receive:
- A user's research query
- A chunk of research content produced for that query

Your job is to:
1. Evaluate whether the content is relevant and factually aligned with the query.
2. Revise the content to make it more accurate, relevant, and focused on the user's research intent.
3. Improve the logical flow, but do not add unrelated information.

Do not include commentary or justification.

## Research Query:
{query}

## Research Text:
{chunk}

## Revised Content:
"""

revisor_prompt = ChatPromptTemplate.from_messages(
    [
        ("system", revisor_template),
        ("human", "query: \n\n {query} \n\n research: \n\n {chunk}")
    ]
)

revisor_chain: RunnableSequence = revisor_prompt | llm