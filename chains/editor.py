from dotenv import load_dotenv
# Load environment variables from a .env file
load_dotenv()

from variables import llm
from langchain_core.runnables import RunnableSequence
from langchain_core.prompts import ChatPromptTemplate


# Define the planner prompt
editor_template = """
You are a research assistant and editor responsible for structuring a revised research text into a formal research-style article.

## Goal:
- Structure the content into standard academic sections:
  - Introduction
  - Background
  - Methodology
  - Results
  - Discussion
  - Conclusion

## Input:
User Query:
{query}

Revised Research Text:
{revised_text}

## Instructions:
- Use formal academic tone.
- Write clear section headers.
- Do NOT add fictional data or unsupported claims.
- Indicate the whole texts into these 6 defined section.
- Modify texts from different topics in a cohesive united text.

## Output:
Provide the full structured article below.
"""

editor_prompt = ChatPromptTemplate.from_messages(
    [
        ("system", editor_template),
        ("human", "query: \n\n {query} \n\n revised text: \n\n {revised_text}")
    ]
)

editor_chain: RunnableSequence = editor_prompt | llm