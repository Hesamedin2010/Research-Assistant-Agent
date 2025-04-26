from typing import Any, List, TypedDict

# This in the input of our nodes and what nodes will update
class GraphState(TypedDict):
    """
    Represents the state of the graph.
    Attributes:
    query: the subject that user wants to create the research about
    plan: tasks that you are going to do to solve the problem and write the atticle
    research: you do the research about each tasks in the plan list
    revised_text: the text and revision
    edited_text: edit the text in a research format

    references: URLs of websites that information are gathered
    search_again: if the agent needs to search again for specific parts
    """
    query: str
    plan: List[str]
    research: List[str]
    revised_text: str
    edited_text: str
    references: List[str]
    search_again: bool