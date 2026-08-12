# 🤖 Web Search AI Agent

> An advanced AI-powered web research assistant built with **Streamlit, Groq, Phi, and DuckDuckGo**. The application combines a large language model with real-time web search to answer questions that require up-to-date information.

![Python](https://img.shields.io/badge/Python-3.10%2B-blue?logo=python)
![Streamlit](https://img.shields.io/badge/Streamlit-App-red?logo=streamlit)
![Groq](https://img.shields.io/badge/Groq-Llama%203.3%2070B-orange)
![Phi](https://img.shields.io/badge/Phi-AI%20Agent-purple)
![License](https://img.shields.io/badge/License-MIT-green)

---

## 📌 Overview

**Web Search AI Agent** is a conversational AI application designed to provide intelligent answers using a combination of:

* 🧠 **Llama 3.3 70B** through Groq for natural-language reasoning
* 🌐 **DuckDuckGo** for web search
* 🤖 **Phi Agent** for agent orchestration and tool execution
* 🎨 **Streamlit** for the interactive web interface
* 🔐 **Streamlit Secrets / Environment Variables** for secure API-key management
* 💬 **Session State** for maintaining conversation history

Unlike a traditional chatbot that relies only on its pretrained knowledge, this application can use web search when a question requires **current or time-sensitive information**.

---

# ✨ Features

## 🧠 AI-Powered Question Answering

The application uses:

```text
Llama 3.3 70B
        ↓
      Groq
        ↓
    Phi Agent
        ↓
DuckDuckGo Search
        ↓
    Final Answer
```

The model can understand the user's question, determine when web information is required, search the web, and generate a response.

---

## 🌐 Real-Time Web Search

The agent is configured to search the web whenever the question requires current information.

Examples:

```text
What are today's top news stories in India?
```

```text
What is the latest OpenAI announcement?
```

```text
Who won yesterday's cricket match?
```

```text
What is the current price of Bitcoin?
```

This makes the application more useful for research and time-sensitive questions.

---

## 💬 ChatGPT-Style Interface

The application provides a conversational interface using Streamlit's:

```python
st.chat_input()
```

and:

```python
st.chat_message()
```

Users can ask multiple questions without restarting the application.

Example:

```text
User:
What happened in the Indian stock market today?

AI:
[Web-powered answer]

User:
Which companies were affected the most?

AI:
[Context-aware follow-up answer]
```

---

## 🗂️ Conversation History

The application stores messages using Streamlit Session State:

```python
st.session_state.messages
```

Messages are stored in the following structure:

```python
{
    "role": "user",
    "content": "Your question"
}
```

and:

```python
{
    "role": "assistant",
    "content": "AI response"
}
```

This allows previous messages to remain visible during the current session.

---

## ⚡ Groq LLM Inference

The application uses Groq with:

```text
llama-3.3-70b-versatile
```

Groq provides high-speed inference, making the application responsive even when generating relatively detailed answers.

---

## 🔎 DuckDuckGo Integration

The agent uses the DuckDuckGo tool:

```python
tools=[DuckDuckGo()]
```

This gives the AI agent access to web-search functionality.

The agent is instructed to:

```text
Always search the web when the question requires current information.
Always include sources in your answer.
```

---

## 🔐 Secure API Key Management

The application supports two methods of loading the Groq API key:

```python
api_key = st.secrets.get("GROQ_API_KEY") or os.getenv("GROQ_API_KEY")
```

### Local Development

You can use an environment variable:

```text
GROQ_API_KEY=your_api_key
```

### Streamlit Cloud

Use Streamlit's Secrets management:

```toml
GROQ_API_KEY = "your_api_key"
```

> ⚠️ Never commit your real API key to GitHub.

---

# 🏗️ Architecture

```text
                        ┌─────────────────────┐
                        │       User          │
                        └──────────┬──────────┘
                                   │
                                   ▼
                        ┌─────────────────────┐
                        │   Streamlit UI      │
                        │   st.chat_input()   │
                        └──────────┬──────────┘
                                   │
                                   ▼
                        ┌─────────────────────┐
                        │    Phi AI Agent     │
                        │     Web Agent       │
                        └──────────┬──────────┘
                                   │
                     ┌─────────────┴─────────────┐
                     │                           │
                     ▼                           ▼
             ┌───────────────┐          ┌────────────────┐
             │  Groq / Llama │          │   DuckDuckGo   │
             │    3.3 70B    │          │   Web Search   │
             └───────┬───────┘          └───────┬────────┘
                     │                           │
                     └─────────────┬─────────────┘
                                   │
                                   ▼
                        ┌─────────────────────┐
                        │   Generated Answer  │
                        └──────────┬──────────┘
                                   │
                                   ▼
                        ┌─────────────────────┐
                        │    Streamlit UI     │
                        └─────────────────────┘
```

---

# 🔄 Application Workflow

The complete workflow is:

```text
1. User enters a question
             ↓
2. Streamlit receives the question
             ↓
3. Question is sent to Phi Agent
             ↓
4. Agent determines whether web search is needed
             ↓
5. DuckDuckGo searches the web
             ↓
6. Search information is provided to the LLM
             ↓
7. Llama 3.3 70B generates the response
             ↓
8. Response is returned to Streamlit
             ↓
9. Answer is displayed to the user
             ↓
10. Conversation is stored in session state
```

---

# 📁 Project Structure

Recommended repository structure:

```text
ai-agent/
│
├── app.py
├── requirements.txt
├── README.md
├── .gitignore
│
└── .streamlit/
    └── secrets.toml
```

For local development, you may alternatively use:

```text
.env
```

instead of `secrets.toml`.

---

# 🛠️ Tech Stack

| Technology      | Purpose                     |
| --------------- | --------------------------- |
| Python          | Application development     |
| Streamlit       | Web UI                      |
| Phi             | AI agent framework          |
| Groq            | LLM inference               |
| Llama 3.3 70B   | Language model              |
| DuckDuckGo      | Web search                  |
| python-dotenv   | Local environment variables |
| Git/GitHub      | Version control             |
| Streamlit Cloud | Deployment                  |

---

# 🚀 Getting Started

## 1. Clone the Repository

```bash
git clone https://github.com/YOUR_USERNAME/ai-agent.git
```

Move into the project:

```bash
cd ai-agent
```

---

## 2. Create a Virtual Environment

### Windows

```bash
python -m venv .venv
```

Activate it:

```bash
.venv\Scripts\activate
```

### macOS / Linux

```bash
python3 -m venv .venv
```

```bash
source .venv/bin/activate
```

---

## 3. Install Dependencies

Create:

```text
requirements.txt
```

Add:

```text
streamlit
phidata
groq
duckduckgo-search
python-dotenv
```

Then install:

```bash
pip install -r requirements.txt
```

---

# 🔑 Configure API Key

## Option 1 — Environment Variable

Create a `.env` file:

```text
GROQ_API_KEY=your_groq_api_key
```

Make sure `.env` is included in `.gitignore`:

```text
.env
.venv/
__pycache__/
```

---

## Option 2 — Streamlit Secrets

Create:

```text
.streamlit/secrets.toml
```

Add:

```toml
GROQ_API_KEY = "your_groq_api_key"
```

The application will automatically read the key using:

```python
st.secrets.get("GROQ_API_KEY")
```

---

# ▶️ Run the Application

Start Streamlit:

```bash
streamlit run app.py
```

The application will normally be available at:

```text
http://localhost:8501
```

---

# ☁️ Deploy to Streamlit Cloud

## Step 1 — Push to GitHub

```bash
git add .
git commit -m "Initial Web Search AI Agent"
git push origin main
```

## Step 2 — Create Streamlit App

Connect your GitHub repository to Streamlit Cloud.

Select:

```text
Main file:
app.py
```

## Step 3 — Configure Secrets

In Streamlit Cloud, open:

```text
App Settings → Secrets
```

Add:

```toml
GROQ_API_KEY = "your_groq_api_key"
```

Deploy the application.

---

# ⚙️ Agent Configuration

The core agent is created with:

```python
Agent(
    name="Web Agent",
    model=Groq(
        id="llama-3.3-70b-versatile",
        api_key=api_key
    ),
    tools=[DuckDuckGo()],
    instructions=[
        "Always search the web when the question requires current information.",
        "Always include sources in your answer.",
    ],
    show_tool_calls=True,
    markdown=True,
)
```

### Agent Components

### Name

```python
name="Web Agent"
```

Identifies the AI agent.

### Model

```python
Groq(
    id="llama-3.3-70b-versatile"
)
```

Provides the underlying LLM.

### Tools

```python
tools=[DuckDuckGo()]
```

Provides web-search capabilities.

### Instructions

```python
instructions=[
    "Always search the web when the question requires current information.",
    "Always include sources in your answer.",
]
```

Controls agent behavior.

### Markdown

```python
markdown=True
```

Allows formatted responses.

### Tool Calls

```python
show_tool_calls=True
```

Allows tool execution details to be exposed by the agent framework.

---

# ⚡ Performance Optimization

The application uses:

```python
@st.cache_resource
```

for agent initialization.

```python
@st.cache_resource
def create_agent():
    return Agent(...)
```

This prevents unnecessary recreation of the agent every time Streamlit reruns the script.

Without caching:

```text
User Input
   ↓
Streamlit rerun
   ↓
Create Agent
   ↓
Run Agent
```

With caching:

```text
First Run
   ↓
Create Agent
   ↓
Cache Agent

Future Runs
   ↓
Reuse Cached Agent
```

This can significantly improve application responsiveness.

---

# 🧠 Session State Management

Streamlit reruns the Python script whenever the user interacts with the UI.

Therefore, conversation history is stored using:

```python
st.session_state.messages
```

Initialization:

```python
if "messages" not in st.session_state:
    st.session_state.messages = []
```

User messages:

```python
st.session_state.messages.append({
    "role": "user",
    "content": question
})
```

Assistant messages:

```python
st.session_state.messages.append({
    "role": "assistant",
    "content": answer
})
```

---

# 🛡️ Error Handling

The application handles agent errors using:

```python
try:
    response = web_agent.run(question)
except Exception as e:
    st.error(f"Error: {str(e)}")
```

This prevents an agent/API failure from completely crashing the UI.

The application also validates the API key:

```python
if not api_key:
    st.error("Missing GROQ_API_KEY.")
    st.stop()
```

---

# 🧪 Example Queries

Try questions such as:

### Current News

```text
What are today's top news stories in India?
```

### Technology

```text
What are the latest developments in artificial intelligence?
```

### Companies

```text
What are the latest announcements from OpenAI?
```

### Research

```text
What are the latest trends in generative AI?
```

### Sports

```text
What happened in today's major cricket matches?
```

### Follow-up Questions

```text
What are today's major AI news stories?
```

Then:

```text
Which company announced the most important update?
```

---

# 🔒 Security Best Practices

Never hard-code your API key:

❌ Don't do this:

```python
api_key = "gsk_xxxxxxxxxxxxx"
```

Use:

```python
api_key = st.secrets.get("GROQ_API_KEY") or os.getenv("GROQ_API_KEY")
```

Also add:

```text
.env
.streamlit/secrets.toml
.venv/
__pycache__/
```

to `.gitignore`.

If an API key is accidentally pushed to GitHub, revoke it immediately and generate a new one.

---

# 🐛 Troubleshooting

## `ModuleNotFoundError: No module named 'streamlit'`

Install:

```bash
pip install streamlit
```

---

## `ModuleNotFoundError: No module named 'dotenv'`

Install:

```bash
pip install python-dotenv
```

and make sure `requirements.txt` contains:

```text
python-dotenv
```

---

## `ModuleNotFoundError: No module named 'phi'`

Install the Phi package used by your project and verify the package/import versions in `requirements.txt`.

---

## `Missing GROQ_API_KEY`

For local development:

```text
GROQ_API_KEY=your_key
```

For Streamlit Cloud:

```toml
GROQ_API_KEY = "your_key"
```

in Streamlit Secrets.

---

## Streamlit App Doesn't Update

Restart the application:

```bash
streamlit run app.py
```

For Streamlit Cloud, trigger a reboot/redeploy after updating dependencies or secrets.

---

# 🚧 Current Limitations

The current version is intentionally lightweight.

### Conversation memory

Conversation history is stored only in:

```python
st.session_state
```

Therefore, it is not persistent across browser sessions or application restarts.

### Search dependency

Web-search functionality depends on the availability and behavior of the configured DuckDuckGo tool.

### API dependency

The application requires a valid Groq API key.

### No persistent database

The application currently does not use PostgreSQL, MySQL, SQLite, Redis, or another persistent storage system.

---

# 🔮 Future Improvements

Possible upgrades include:

* [ ] Persistent conversation history
* [ ] User authentication
* [ ] Multiple chat sessions
* [ ] New Chat button
* [ ] Sidebar conversation history
* [ ] Streaming LLM responses
* [ ] Better source cards
* [ ] Search-result previews
* [ ] PDF/document upload
* [ ] RAG pipeline
* [ ] Vector database integration
* [ ] Long-term memory
* [ ] Conversation export
* [ ] Download answers as PDF/Markdown
* [ ] Voice input
* [ ] Voice output
* [ ] Multi-agent architecture
* [ ] Search provider fallback
* [ ] Response evaluation
* [ ] Rate limiting
* [ ] Production logging
* [ ] Analytics dashboard

---

# 🧩 Possible Advanced Architecture

A future production version could evolve into:

```text
                         ┌───────────────┐
                         │     User      │
                         └───────┬───────┘
                                 │
                                 ▼
                     ┌──────────────────────┐
                     │    Streamlit UI      │
                     └──────────┬───────────┘
                                │
                                ▼
                     ┌──────────────────────┐
                     │   Agent Router       │
                     └──────────┬───────────┘
                                │
             ┌──────────────────┼──────────────────┐
             │                  │                  │
             ▼                  ▼                  ▼
      ┌────────────┐    ┌────────────┐    ┌────────────┐
      │ Web Agent  │    │ RAG Agent  │    │ Data Agent │
      └─────┬──────┘    └─────┬──────┘    └─────┬──────┘
            │                  │                  │
            ▼                  ▼                  ▼
       Web Search         Vector DB          Data Sources
            │                  │                  │
            └──────────────────┼──────────────────┘
                               │
                               ▼
                      ┌─────────────────┐
                      │   LLM / Groq    │
                      └────────┬────────┘
                               │
                               ▼
                      ┌─────────────────┐
                      │ Final Response  │
                      └─────────────────┘
```

This would turn the project from a simple web-search chatbot into a more complete **AI Agent platform**.

---

# 📊 Project Highlights

This project demonstrates practical experience with:

* AI Agents
* LLM integration
* Prompt/instruction engineering
* Tool calling
* Web search
* Real-time information retrieval
* Streamlit application development
* API integration
* Environment/secrets management
* Session-state management
* Error handling
* Cloud deployment

---

# 💼 Resume Project Description

You can describe the project on your resume as:

> **Web Search AI Agent | Python, Streamlit, Groq, Llama 3.3, Phi, DuckDuckGo**
> Developed an AI-powered conversational web agent using Llama 3.3 70B and Groq for high-speed inference, integrated DuckDuckGo web search for real-time information retrieval, and built an interactive Streamlit interface with session-based conversation history and secure API-key management.

---

# 📜 License

This project is available under the **MIT License**.

You are free to use, modify, and distribute the project according to the terms of the license.

---

# 👨‍💻 Author

**Satyam Pandey**

AI/ML Developer | Python | Machine Learning | Generative AI | AI Agents

---

# ⭐ Support

If you find this project useful:

⭐ Star the repository
🍴 Fork the repository
🐛 Report issues
💡 Suggest improvements
🚀 Build something on top of it

---

## 🚀 Final Goal

The long-term goal of this project is to evolve from a simple web-search chatbot into a **production-ready AI research agent** capable of:

```text
Understand → Search → Reason → Verify → Synthesize → Cite
```

giving users a reliable conversational interface for researching current information from the web.
