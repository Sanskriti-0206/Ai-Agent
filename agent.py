import os
import streamlit as st

from phi.agent import Agent
from phi.model.groq import Groq
from phi.tools.duckduckgo import DuckDuckGo


# --------------------------------------------------
# PAGE CONFIG
# --------------------------------------------------

st.set_page_config(
    page_title="Web Search AI Agent",
    page_icon="🤖",
    layout="wide"
)


# --------------------------------------------------
# LOAD ENVIRONMENT VARIABLES
# --------------------------------------------------

api_key = st.secrets.get("GROQ_API_KEY") or os.getenv("GROQ_API_KEY")

if not api_key:
    st.error("Missing GROQ_API_KEY. Add it to Streamlit Cloud secrets or your environment.")
    st.stop()


# --------------------------------------------------
# CUSTOM CSS
# --------------------------------------------------

st.markdown("""
<style>

.main-title {
    font-size: 40px;
    font-weight: 700;
    text-align: center;
    margin-bottom: 5px;
}

.subtitle {
    text-align: center;
    color: #888888;
    font-size: 18px;
    margin-bottom: 30px;
}

.stChatMessage {
    border-radius: 12px;
}

</style>
""", unsafe_allow_html=True)


# --------------------------------------------------
# HEADER
# --------------------------------------------------

st.markdown(
    '<div class="main-title">🤖 Web Search AI Agent</div>',
    unsafe_allow_html=True
)

st.markdown(
    '<div class="subtitle">Ask anything and get answers using live web search</div>',
    unsafe_allow_html=True
)


# --------------------------------------------------
# CREATE AGENT
# --------------------------------------------------

@st.cache_resource
def create_agent():

    return Agent(
        name="Web Agent",
        model=Groq(
            id="llama-3.3-70b-versatile",
            api_key=api_key
        ),
        tools=[DuckDuckGo()],
        instructions=[
            "Always search the web when the question requires current information.",
            "Always include sources in your answer.",
            "Always use the DuckDuckGo search tool for every prompt given by the user, regardless of whether you think you already know the answer.",
            "Before providing your final answer, explicitly summarize the search results you found.",
            "Always include URLs and sources in your answer.",
        ],
        show_tool_calls=True,
        markdown=True,
    )


web_agent = create_agent()


# --------------------------------------------------
# SESSION STATE
# --------------------------------------------------

if "messages" not in st.session_state:
    st.session_state.messages = []


# --------------------------------------------------
# DISPLAY PREVIOUS CHAT
# --------------------------------------------------

for message in st.session_state.messages:

    with st.chat_message(message["role"]):

        st.markdown(message["content"])


# --------------------------------------------------
# USER INPUT
# --------------------------------------------------

question = st.chat_input(
    "Ask your question..."
)


# --------------------------------------------------
# PROCESS QUESTION
# --------------------------------------------------

if question:

    # Display user question
    with st.chat_message("user"):
        st.markdown(question)

    # Save user message
    st.session_state.messages.append({
        "role": "user",
        "content": question
    })

    # Generate response
    with st.chat_message("assistant"):

        with st.spinner("🔎 Searching the web and generating answer..."):

            try:

                response = web_agent.run(question)

                # Extract response text
                answer = response.content

                st.markdown(answer)

                # Save assistant response
                st.session_state.messages.append({
                    "role": "assistant",
                    "content": answer
                })

            except Exception as e:

                st.error(f"Error: {str(e)}")
