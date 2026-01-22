# 🤖 Multi-Agent Research Assistant

An intelligent research tool built with **LangGraph**, **Groq (Llama 3.3)**, and **Tavily**. This application uses a state-machine approach to decide whether it can answer a question from internal knowledge or if it needs to browse the live web for the most up-to-date information.

## 🌟 Features
* **Autonomous Decision Making**: Uses an LLM "Analyzer" node to determine if a query requires a live web search or can be answered from general knowledge.
* **Live Web Search**: Integrated with **Tavily Search API** to fetch high-quality, research-oriented results.
* **Professional UI**: A sleek **Streamlit** dashboard with a sidebar for secure API key management and an interactive "Agent Status" tracker.
* **Full Transparency**: Users can view the internal "steps" taken by the agent and see raw data retrieved from the web.

## 📁 Project Structure
* **`agentic-app.py`**: **The primary application file.** Use this to launch the full web-based Graphical User Interface (GUI).
* **`main.py`**: The core logic engine and CLI version. It defines the `ResearchState` and the LangGraph nodes for analysis, searching, and synthesis, including environment variable loading via `python-dotenv`.
* **`Tests_Scriptfiles/`**: Contains utility scripts and connection tests, such as `tavily-connection.py`, to verify API integrations independently before running the full workflow.
* **`requirements.txt`**: List of Python dependencies including `streamlit`, `langgraph`, `langchain-groq`, and `tavily-python`.
* **`.gitignore`**: Protects your sensitive `GROQ_API_KEY` and `TAVILY_API_KEY` by ignoring `.env` and temporary files.

## 🚀 Getting Started

### 1. Clone the Repository
Run this command to pull the project to your local machine:
```bash
git clone [https://github.com/PavithraPN-01/Agent-lgls-stack.git](https://github.com/PavithraPN-01/Agent-lgls-stack.git)
cd Agent-lgls-stack

```
### 2.Run the Research Assistant
Run this command  to launch the full Graphical User Interface (GUI):

```bash
streamlit run agentic-app.py

```


