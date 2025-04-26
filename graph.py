from consts import PLANNING, WEBSEARCH, REVISE, EDIT, PUBLISH_DOCX
from nodes.research_topic import planning
from nodes.search import websearch
from nodes.revise import revise
from nodes.edit import edit
from nodes.create_docx import publish_docx
from state import GraphState
from langgraph.graph import StateGraph, END

workflow = StateGraph(GraphState)

# Define the first node
workflow.set_entry_point(PLANNING)

# Add nodes
workflow.add_node(PLANNING, planning)
workflow.add_node(WEBSEARCH, websearch)
workflow.add_node(REVISE, revise)
workflow.add_node(EDIT, edit)
workflow.add_node(PUBLISH_DOCX, publish_docx)

# Add edges
workflow.add_edge(PLANNING, WEBSEARCH)
workflow.add_edge(WEBSEARCH, REVISE)
workflow.add_edge(REVISE, EDIT)
workflow.add_edge(EDIT, PUBLISH_DOCX)
workflow.add_edge(PUBLISH_DOCX, END)

app = workflow.compile()

