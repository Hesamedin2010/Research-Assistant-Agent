# AI-Powered Research Assistant

## Problem Statement

In today’s fast-paced information environment, researchers, students, and professionals often need to quickly compile structured research reports.  
Manually planning sub-topics, finding reliable information, revising content, and formatting academic sections is slow and repetitive.

**Problem I chose to solve:**  
> Build an autonomous AI agent that takes any research query and automatically generates a formal, structured research article — including Introduction, Background, Methodology, Results, Discussion, and Conclusion — with minimal human intervention.

---

## ⚙️ System Architecture and Reasoning

This project is designed as a **modular, extensible autonomous agent** using **LangChain**, **LangGraph**, and **Streamlit**.

The system demonstrates:
- **Autonomous Reasoning** (ReAct-style loop: plan → search → revise → edit)
- **Tool Use** (web search API, document generation)
- **Short-term Memory** (current task state in LangGraph)
- **Long-term Memory** (semantic memory with FAISS + FastEmbed)
- **Error-Resilient Design** (semantic chunking, token-safe editing)

### Architecture Overview


### Key Components

| Module | Description |
|---|---|
| `chains/` | LLM tasks: planner, researcher, revisor, editor |
| `nodes/` | LangGraph nodes: handle state transitions |
| `state.py` | Defines the research state (query, plan, research, edits, references) |
| `memory.py` | JSON-based or semantic FAISS long-term memory |
| `semantic_memory.py` | Vector database (FAISS + FastEmbed) |
| `graph.py` | Full research workflow graph |
| `user-interface.py` | Streamlit UI for input, history, and downloads |

---

## Instructions for Running the Project

### 1. Clone the Repository

```bash
git clone https://github.com/your-username/research-assistant-agent.git
cd research-assistant-agent
```
### 2. Install Dependencies (with Pipenv)
```
pip install pipenv  # Only if Pipenv isn't installed yet
pipenv install
```
### 3. Activate the Virtual Environment
```
pipenv shell
```
### 4. Set Environment Variables
```
GROQ_API_KEY=your-groq-api-key
TAVILY_API_KEY=your-tavily-api-key
```
### 5. Run the Streamlit App
```
Run the Streamlit App
```

## Key Features
✅ Autonomous multi-step research agent
✅ Task planning, live web search, semantic revision, and academic editing
✅ Semantic chunking to handle large texts without hitting token limits
✅ Long-term memory with FAISS + FastEmbed for faster repeated queries
✅ Streamlit UI with research history panel and download buttons
✅ Modular design: easily extend nodes, swap LLMs, or add new tools

### Future Extensions
- Multi-agent collaboration (separate planner, researcher, and editor agents communicating)
- More persistent memory (e.g., ChromaDB or dedicated knowledge graph)
- More interactive user feedback after draft generation (Human-In-The-Loop)
