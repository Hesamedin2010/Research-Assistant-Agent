from variables import text_splitter
from chains.revisor import revisor_chain

def revise(state):
    """
    It takes the user's query and a chunk of text in order to check if the achieved texts from web are related to the research
    """
    print("--REVISING--")
    query = state["query"]
    plans = state["plan"]
    searches = state["research"]
    revised_texts = ""

    for search in searches:
      chunks = text_splitter.split_text(search)
      for chunk in chunks:
        revised_text = revisor_chain.invoke({"query": query, "chunk": chunk})
        revised_texts += revised_text.content + "\n"
      state["revised_text"] = revised_texts
    return state