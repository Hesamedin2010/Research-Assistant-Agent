import streamlit as st
import os
from graph import app
from memory import load_memory, save_memory  # long-term memory
from groq import RateLimitError

st.set_page_config(page_title="AI-Agent Research Assistant", layout="wide")

st.title("🧠 AI-Agent Research Assistant")
st.markdown("Enter your research query and get a structured report!")

# --- Input box
query = st.text_area("🔍 Research Topic", placeholder="E.g. Compare solar and wind energy in Europe")

if st.button("🚀 Run Agent"):
    if not query.strip():
        st.warning("Please enter a research topic.")
    else:
        try:
            with st.spinner("Running the research agent..."):
                result = app.invoke(input={"query": query})

                st.success("✅ Research Completed!")

                # Save to memory
                if "edited_text" in result and "pdf_path" in result:
                    save_memory({
                        "query": result.get("query", query),
                        "pdf_path": result["pdf_path"]
                    })

                # Show result preview
                st.subheader("📄 Final Report Preview")
                st.markdown(result["edited_text"])

                # Download link
                if "pdf_path" in result:
                    file_path = result["pdf_path"]
                    with open(file_path, "rb") as f:
                        st.download_button(
                            label="📥 Download Report",
                            data=f,
                            file_name=os.path.basename(file_path),
                            mime="application/vnd.openxmlformats-officedocument.wordprocessingml.document"
                            if file_path.endswith(".docx") else "application/pdf"
                        )
        except RateLimitError as e:
            st.error(
                "🚫 You’ve hit your daily token limit for the Groq API. Please wait and try again later or upgrade your plan.")

# --- History Panel
st.sidebar.title("🧠 Research History")
past_queries = load_memory()

if past_queries:
    for item in reversed(past_queries[-5:]):  # Show only last 5
        st.sidebar.markdown(f"**• {item['query']}**")
        if os.path.exists(item["pdf_path"]):
            with open(item["pdf_path"], "rb") as f:
                st.sidebar.download_button(
                    label="Download",
                    data=f,
                    file_name=os.path.basename(item["pdf_path"]),
                    key=item["pdf_path"]
                )
else:
    st.sidebar.info("No past research yet.")
