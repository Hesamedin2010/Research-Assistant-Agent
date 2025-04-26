import json
import os

MEMORY_PATH = "memory.json"

def load_memory():
    if os.path.exists(MEMORY_PATH):
        with open(MEMORY_PATH, "r") as f:
            try:
                return json.load(f)
            except json.JSONDecodeError:
                print("⚠️ Warning: memory.json is empty or corrupted. Resetting memory.")
                return []  # Return an empty memory safely
    return []

def save_memory(entry):
    memory = load_memory()
    memory.append(entry)
    with open(MEMORY_PATH, "w") as f:
        json.dump(memory, f, indent=2)

def search_memory(query_keywords: list[str]):
    memory = load_memory()
    return [m for m in memory if any(k.lower() in m["query"].lower() for k in query_keywords)]
