from langchain_community.tools.tavily_search import TavilySearchResults
from memory import search_memory
from semantic_memory import search_semantic_memory

web_search_tool = TavilySearchResults(max_results=3)

def websearch(state):
    """
    This function searches for each sub-topic in the research plan.
    It first tries to retrieve from semantic memory, otherwise it does a live web search.
    """
    print("---WEB SEARCH---")
    query = state["query"]
    plans = state["plan"]
    searches = []
    references = []

    for plan in plans:
        print(f"🔎 Searching for sub-topic: {plan}")

        # First try: Semantic search in memory
        # semantic_hits = search_memory(plan, k=1)  # key-word based memory
        semantic_hits = search_semantic_memory(plan, k=1)  # semantic memory
        if semantic_hits:
            print(f"✅ Found from memory for: {plan}")
            searches.append(semantic_hits[0].page_content)

            if "references" in semantic_hits[0].metadata:
                references.extend(semantic_hits[0].metadata["references"])

        else:
            # Live Web search
            print(f"🌐 No memory found. Doing live web search for: {plan}")
            tavily_results = web_search_tool.invoke({"query": plan})

            # Merge the text results into a single big chunk
            joined_tavily_results = "\n".join(
                [r["content"] for r in tavily_results]
            )
            searches.append(joined_tavily_results)

            references.extend([r["url"] for r in tavily_results])

    # Save results to state
    state["research"] = searches
    state["references"] = list(set(references))  # Remove duplicate URLs
    return state