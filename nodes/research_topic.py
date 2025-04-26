from chains.planner import planner_chain
from memory import search_memory

def planning(state):
    """
    It takes the user's query in order to break it into subjects to research deeper
    """
    print("--TASK PLANNING--")
    query = state["query"]
    state["search_again"] = False
    # Check memory for similar past queries
    past = search_memory(query.lower().split())
    if past:
        stashed = past[-1]
        state["plan"] = [f"(Reused) {stashed['query']}"]
        return state
    # Else, generate a plan
    plans = planner_chain.invoke({"query": query})
    print("\nGenerated Plan:\n", plans)
    plans_list = plans.content.split(",")
    state["plan"] = plans_list
    return state