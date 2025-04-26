from variables import text_splitter
from chains.editor import editor_chain

def estimate_token_count(text: str) -> int:
    """
    Rough estimation: 1 token ~ 4 characters (depends on language/model).
    """
    return len(text) // 4

def edit(state):
    """
    Takes the full revised text, splits it into semantic chunks,
    selects as much as allowed, and edits into a formal research paper.
    """
    print("--TEXT EDITING--")
    query = state["query"]
    revised_texts = state["revised_text"]

    safe_token_limit = 10000  # Stay under 10k tokens to be very safe (Groq limit ~12k tokens)

    # Semantic split of full revised text
    chunks = text_splitter.split_text(revised_texts)

    selected_chunks = []
    total_tokens = 0

    # 2. Add chunks until we reach safe limit
    for chunk in chunks:
        chunk_tokens = estimate_token_count(chunk)
        if total_tokens + chunk_tokens <= safe_token_limit:
            selected_chunks.append(chunk)
            total_tokens += chunk_tokens
        else:
            break

    merged_revised_text = "\n\n".join(selected_chunks)

    # Pass the merged text to editor chain
    edited = editor_chain.invoke({
        "query": query,
        "revised_text": merged_revised_text
    })

    state["edited_text"] = edited.content
    return state


