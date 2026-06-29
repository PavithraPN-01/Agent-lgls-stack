
# 🔍 Multi-Agent Research Assistant using LangGraph, Groq & Tavily

<p align="center">

<img src="https://img.shields.io/badge/Python-3.11-blue?style=for-the-badge&logo=python">

<img src="https://img.shields.io/badge/LangGraph-Agentic%20AI-success?style=for-the-badge">

<img src="https://img.shields.io/badge/LangChain-Framework-green?style=for-the-badge">

<img src="https://img.shields.io/badge/Groq-Llama%203.3-orange?style=for-the-badge">

<img src="https://img.shields.io/badge/Tavily-Web%20Search-red?style=for-the-badge">

<img src="https://img.shields.io/badge/Streamlit-Web%20Application-ff4b4b?style=for-the-badge&logo=streamlit">

<img src="https://img.shields.io/badge/License-MIT-yellow?style=for-the-badge">

</p>

---

# 📖 Project Overview

The **Multi-Agent Research Assistant** is an intelligent **Agentic AI application** that demonstrates how multiple AI agents collaborate to answer user queries using **LangGraph**, **Groq's Llama 3.3**, and the **Tavily Search API**.

Unlike traditional AI chatbots that rely solely on a Large Language Model (LLM), this project introduces an intelligent decision-making workflow capable of determining whether a user's query can be answered using the model's internal knowledge or whether it requires real-time information from the internet.

The workflow begins with a **Query Analysis Agent**, which evaluates the user's question. If the query involves current events, recent developments, or dynamic information, the system automatically invokes the **Tavily Search Agent** to retrieve relevant web content. The retrieved information is then passed to a **Synthesis Agent**, which generates a comprehensive and structured response using the Groq-hosted Llama 3.3 model.

For general knowledge questions, the workflow bypasses web search entirely and directly generates an answer using the language model, reducing latency and unnecessary API calls.

The project demonstrates practical implementation of **Agentic AI**, **conditional routing**, **tool calling**, **state management**, and **workflow orchestration**, making it an excellent learning project for modern AI application development.

---

# 🚀 Why This Project?

Modern AI assistants such as ChatGPT, Claude, Gemini, and Perplexity combine reasoning with external tools to provide accurate and up-to-date information.

This project was developed to understand how autonomous AI systems decide when to use their internal knowledge and when to retrieve external information. Rather than building a conventional chatbot, the goal was to create an intelligent multi-agent workflow that can make decisions, execute different tasks, and provide explainable responses.

The project showcases how Agentic AI systems can intelligently coordinate multiple specialized agents to solve user queries efficiently while maintaining transparency and scalability.

---

# 🎯 Problem Statement

Large Language Models possess extensive knowledge but are limited by the information available during their training.

They cannot reliably answer questions related to:

- Current events
- Breaking news
- Recent research publications
- Latest AI developments
- Market trends
- Dynamic web content

Performing an internet search for every user query is inefficient because it increases response time, API usage, and computational cost.

This project addresses this limitation by introducing an intelligent routing mechanism that determines whether web search is actually required before generating a response.

The result is a faster, smarter, and more resource-efficient AI assistant.

---

# 💡 Objectives

The primary objectives of this project are:

- Build an Agentic AI workflow using LangGraph.
- Demonstrate intelligent decision-making through conditional routing.
- Integrate a Large Language Model using Groq.
- Retrieve live information using the Tavily Search API.
- Generate accurate and well-structured responses.
- Reduce unnecessary web searches.
- Provide transparency by displaying each step of the agent workflow.
- Develop both a Command-Line Interface (CLI) and a Streamlit-based web application.

---

# ✨ Key Features

## 🤖 Intelligent Query Analysis

The application first analyzes every user query to determine whether external information is required.

Benefits:

- Faster responses
- Reduced API usage
- Efficient workflow execution

---

## 🌐 Live Web Search

When recent information is required, the application automatically performs a web search using the Tavily Search API.

Features include:

- Research-oriented search
- Trusted sources
- Relevant content retrieval
- Configurable number of search results

---

## 🧠 Direct Knowledge Answering

General knowledge questions are answered directly using the Groq-hosted **Llama-3.3-70B-Versatile** model.

Advantages:

- Low latency
- No unnecessary internet requests
- Faster response generation

---

## 🔀 Conditional Workflow Routing

LangGraph enables intelligent routing based on the query type.

Example workflow:

General Knowledge Question

```
User Query

↓

Analyze Query

↓

Direct Answer

↓

Final Response
```

Research Query

```
User Query

↓

Analyze Query

↓

Web Search

↓

Synthesize Response

↓

Final Answer
```

---

## 📊 Transparent Agent Execution

The Streamlit application displays the execution steps performed by the AI agents.

Example:

```
🧠 Analyze Query

↓

🌐 Search Web

↓

✍️ Generate Final Response
```

This improves explainability by allowing users to understand how the final answer was produced.

---

## 🖥️ Dual Execution Modes

The project can be executed in two different ways.

### Command-Line Interface (CLI)

The `main.py` file allows developers to test the LangGraph workflow directly from the terminal using predefined sample queries.

### Streamlit Web Application

The `agentic-app.py` file provides an interactive graphical interface where users can enter API keys, submit queries, and observe the workflow in real time.

---

# 🏗️ System Architecture

```
                    User Query
                         │
                         ▼
              ┌────────────────────┐
              │  Analyze Agent     │
              └────────────────────┘
                         │
          ┌──────────────┴──────────────┐
          │                             │
          ▼                             ▼
   Needs Web Search?              Direct Answer
          │                             │
          ▼                             ▼
 ┌──────────────────┐          ┌──────────────────┐
 │ Tavily Search    │          │ Groq LLM         │
 └──────────────────┘          └──────────────────┘
          │
          ▼
 ┌──────────────────┐
 │ Synthesis Agent  │
 └──────────────────┘
          │
          ▼
     Final Response
```

---

# ⚙️ How It Works

The workflow follows these steps:

1. The user submits a query.

2. The Query Analysis Agent determines whether the query requires recent information.

3. If recent information is required, the workflow invokes the Tavily Search Agent.

4. The search results are collected and passed to the Synthesis Agent.

5. The Synthesis Agent generates a comprehensive response using the Groq-hosted Llama model.

6. If the query does not require web search, the Direct Answer Agent immediately generates the response using the LLM.

7. The final response and workflow execution steps are displayed to the user.

---

# 🧠 AI Agents

The project consists of four specialized AI agents.

## Agent 1 – Query Analysis Agent

Responsibilities:

- Understand user intent
- Analyze the query
- Decide whether web search is required
- Route the workflow

---

## Agent 2 – Web Search Agent

Responsibilities:

- Retrieve information from the internet
- Use the Tavily Search API
- Collect relevant sources
- Pass search results to the Synthesis Agent

---

## Agent 3 – Synthesis Agent

Responsibilities:

- Read retrieved search results
- Summarize information
- Generate a structured response
- Preserve important facts

---

## Agent 4 – Direct Answer Agent

Responsibilities:

- Handle general knowledge questions
- Generate responses using the LLM
- Avoid unnecessary web searches
- Improve response speed


# 🛠️ Technology Stack

The Multi-Agent Research Assistant is built using modern Generative AI frameworks and tools that enable intelligent workflow orchestration, natural language understanding, and live web information retrieval.

| Technology | Purpose |
|------------|---------|
| **Python 3.11+** | Core programming language |
| **LangGraph** | Multi-agent workflow orchestration |
| **LangChain** | LLM integration framework |
| **Groq API** | High-speed LLM inference |
| **Llama-3.3-70B-Versatile** | Large Language Model |
| **Tavily Search API** | Live web search and retrieval |
| **Streamlit** | Interactive web application |
| **python-dotenv** | Environment variable management |
| **Typing** | State management using TypedDict |
| **Operator** | State aggregation within LangGraph |

---

# 📂 Project Structure

```
Agent-lgls-stack/
│
├── Tests_Scriptfiles/
│   └── tavily-connection.py
│
├── agentic-app.py
├── main.py
├── requirements.txt
├── .env.example
├── .gitignore
├── LICENSE
└── README.md
```

---

# 📁 File Description

## 📌 agentic-app.py

This file provides the Streamlit-based graphical user interface (GUI) for the application.

Responsibilities include:

- Accepting user queries
- Securely collecting Groq and Tavily API keys
- Building the LangGraph workflow
- Executing the workflow
- Displaying agent execution steps
- Showing the final synthesized response
- Displaying raw search results when web search is performed

This serves as the primary user interface of the project.

---

## 📌 main.py

This file contains the complete Agentic AI workflow implementation.

It defines:

- ResearchState
- Query Analysis Agent
- Web Search Agent
- Response Synthesis Agent
- Direct Answer Agent
- Conditional Routing Logic
- LangGraph Workflow

The file also includes predefined sample queries for command-line testing.

---

## 📌 Tests_Scriptfiles/

This folder contains utility scripts used during development.

### tavily-connection.py

A standalone testing script used to verify the Tavily Search API connection before integrating it into the complete workflow.

---

## 📌 .env.example

Provides a template for configuring API keys required by the application.

Example:

```env
groq_api_key = "Paste your Groq API key here"
langsmith_api_key = "Paste your LangSmith API key here"
tavily_api_key = "Paste your Tavily API key here"
```

> **Note:** The current implementation uses only the **Groq** and **Tavily** API keys. The LangSmith key is included as a placeholder for future tracing and observability features.

---

## 📌 requirements.txt

Contains all Python packages required to install and run the application.

---

## 📌 LICENSE

Contains the MIT License for this project.

---

## 📌 README.md

Provides complete documentation, setup instructions, architecture explanation, workflow details, and implementation overview.

---

# 🧠 LangGraph State Management

LangGraph maintains a shared state throughout workflow execution.

The state contains the following variables:

| Variable | Description |
|-----------|-------------|
| **query** | User input |
| **needs_search** | Decision made by the Query Analysis Agent |
| **search_results** | Retrieved web search results |
| **final_answer** | Generated response |
| **steps** | Execution history of the workflow |

Each node updates the shared state before passing it to the next node.

---

# 🔄 Workflow Execution

The LangGraph workflow executes as follows:

```
START

↓

Analyze Query

↓

Needs Web Search?

↓

YES ───────────────► Search Web

│                       │

│                       ▼

│              Retrieve Search Results

│                       │

│                       ▼

│              Synthesize Response

│                       │

│                       ▼

└──────────────► Final Response

NO

↓

Generate Direct Answer

↓

Final Response

↓

END
```

---

# 🔀 Conditional Routing

One of the key features of LangGraph is conditional routing.

Rather than following a fixed execution pipeline, the workflow dynamically changes depending on the user's query.

### Example 1

Query

```
Explain Machine Learning
```

Workflow

```
Analyze

↓

Direct Answer

↓

End
```

---

### Example 2

Query

```
Latest developments in Artificial Intelligence
```

Workflow

```
Analyze

↓

Search Web

↓

Synthesize

↓

End
```

This approach minimizes unnecessary API calls while improving response efficiency.

---

# 🌐 Web Search Integration

The project integrates the **Tavily Search API** to retrieve recent and reliable information from the internet.

Features include:

- Live internet search
- Research-focused results
- Configurable maximum search results
- Reliable source retrieval
- Structured search output

The retrieved information is then passed to the Synthesis Agent for response generation.

---

# 🤖 Large Language Model

The project uses:

## Groq

Model:

```
Llama-3.3-70B-Versatile
```

Reasons for selecting this model:

- High reasoning capability
- Fast inference
- Strong instruction-following performance
- Excellent summarization
- Low latency
- High-quality response generation

---

# 🎨 User Interface

The Streamlit interface provides a simple and interactive user experience.

Features include:

- User query input
- Secure API key entry
- Sidebar configuration panel
- Live workflow status updates
- Final answer display
- Expandable raw search results

The interface allows users to observe the execution of each AI agent in real time.

---

# 🚀 Installation Guide

## Step 1 — Clone the Repository

```bash
git clone https://github.com/PavithraPN-01/Agent-lgls-stack.git

cd Agent-lgls-stack
```

---

## Step 2 — Create a Virtual Environment

### Windows

```bash
python -m venv venv
```

Activate the environment:

```bash
venv\Scripts\activate
```

---

### Linux / macOS

```bash
python3 -m venv venv

source venv/bin/activate
```

---

## Step 3 — Install Dependencies

```bash
pip install -r requirements.txt
```

---

## Step 4 — Configure API Keys

Rename `.env.example` to `.env` and update it with your API keys.

Example:

```env
groq_api_key=YOUR_GROQ_API_KEY
tavily_api_key=YOUR_TAVILY_API_KEY
```

---

## Step 5 — Run the Project

### Option 1 – Command-Line Interface

```bash
python main.py
```

This runs the predefined sample queries and prints the workflow execution in the terminal.

---

### Option 2 – Streamlit Web Application

```bash
streamlit run agentic-app.py
```

The Streamlit application opens automatically in your default web browser.

---

# 🔑 Required API Keys

The project requires the following API keys:

## Groq API

Used for:

- Query Analysis
- Direct Answer Generation
- Response Synthesis

---

## Tavily API

Used for:

- Live Internet Search
- Information Retrieval
- Research-Oriented Queries

---

# 💬 Example Queries

### General Knowledge

```
What is Artificial Intelligence?
```

Expected Workflow

```
Analyze

↓

Direct Answer
```

---

### Current Affairs

```
Latest OpenAI announcements
```

Expected Workflow

```
Analyze

↓

Search

↓

Synthesize
```

---

### Programming

```
Explain LangGraph.
```

Expected Workflow

```
Analyze

↓

Direct Answer
```

---

### Research

```
Recent developments in Quantum Computing
```

Expected Workflow

```
Analyze

↓

Search

↓

Synthesize

↓

Final Response
```

---

# 📊 Sample Output

```
🧠 Decision: Web Search

🌐 Found 3 Sources

✍️ Synthesized Research

---------------------------------

Final Answer:

Artificial Intelligence has recently...
```

---

# 🧪 Testing

The application has been tested using both execution modes.

### Command-Line Testing

- General Knowledge
- Current Affairs
- Programming Concepts
- Artificial Intelligence
- Research Questions

Executed using:

```bash
python main.py
```

---

### Streamlit Testing

The graphical interface was tested for:

- API key validation
- Query processing
- Workflow execution
- Live status updates
- Final answer generation
- Raw search result display

---


# 🌟 Project Highlights

This project demonstrates the practical implementation of **Agentic AI** using a graph-based workflow. Instead of relying solely on a Large Language Model (LLM), the application intelligently decides whether to answer from its internal knowledge or retrieve real-time information from the web.

### Key Highlights

- 🤖 Multi-Agent AI Workflow
- 🔄 Conditional Routing using LangGraph
- 🌐 Live Web Search Integration with Tavily
- 🧠 Intelligent Query Analysis
- ⚡ High-Speed Inference using Groq
- 📚 Research-Oriented Response Generation
- 🎨 Interactive Streamlit Interface
- 🖥️ Command-Line Testing Support
- 🔐 Secure API Key Management
- 📊 Transparent Workflow Execution
- 📝 Well-Structured Response Generation

---

# 📚 Concepts Demonstrated

This project showcases practical implementation of several important Generative AI concepts, including:

- Agentic AI
- LangGraph
- LangChain
- Large Language Models (LLMs)
- Prompt Engineering
- Workflow Orchestration
- State Management
- Conditional Routing
- Tool Calling
- Web Search Integration
- API Integration
- Environment Variable Management
- Streamlit Application Development
- Python Programming
- AI Application Development

---

# 🎯 Skills Demonstrated

The project demonstrates the following technical skills.

### Programming

- Python
- Modular Programming
- Object-Oriented Design
- Code Organization

### Generative AI

- Large Language Models
- Agentic AI
- Workflow Design
- Prompt Engineering
- AI Tool Integration
- Information Retrieval

### Frameworks & Libraries

- LangGraph
- LangChain
- Streamlit

### API Integration

- Groq API
- Tavily Search API

### Software Engineering

- State Management
- Environment Configuration
- Error Handling
- Git & GitHub
- Modular Project Architecture

---

# 🎓 Learning Outcomes

This project provided practical experience in:

- Building an Agentic AI workflow
- Understanding LangGraph execution
- Passing state between workflow nodes
- Integrating external AI tools
- Implementing conditional routing
- Designing explainable AI workflows
- Building interactive AI applications
- Combining reasoning with external knowledge retrieval

---

# 🚧 Challenges Faced

Several challenges were encountered during development, including:

- Understanding LangGraph workflow execution
- Designing an effective query analyzer
- Managing shared workflow state
- Integrating multiple APIs
- Handling environment variables securely
- Building an interactive Streamlit interface
- Reducing unnecessary API calls
- Improving response quality
- Debugging workflow routing

Each challenge contributed to a deeper understanding of real-world AI application development.

---

# 🚀 Future Enhancements

This project serves as a strong foundation for more advanced Agentic AI systems.

Possible future improvements include:

- 💬 Multi-turn conversation support
- 🧠 Long-term conversational memory
- 📄 PDF document analysis
- 📚 Retrieval-Augmented Generation (RAG)
- 🗂️ Vector database integration (FAISS or ChromaDB)
- 🌍 Multi-language support
- 🎙️ Voice-based interaction
- 🖼️ Multimodal input support
- 📈 Workflow analytics dashboard
- 🔍 Source citation formatting
- ☁️ Cloud deployment
- 🐳 Docker containerization
- 👤 User authentication
- 📊 Agent performance monitoring

---

# ⚡ Performance Considerations

The workflow has been designed to improve efficiency by:

- Avoiding unnecessary web searches
- Using conditional routing
- Leveraging Groq's low-latency inference
- Executing only required workflow nodes
- Limiting search results for faster synthesis
- Maintaining lightweight state throughout execution

---

# 🔒 Security

The project follows several security best practices.

Implemented measures include:

- API keys stored outside the source code
- Environment variable configuration
- `.env` excluded using `.gitignore`
- Secure API key entry in the Streamlit interface
- No hardcoded credentials in application logic

---

# 📖 Frequently Asked Questions (FAQ)

## Why use LangGraph?

LangGraph enables conditional workflows, making it possible for AI agents to make intelligent decisions instead of following a fixed execution pipeline.

---

## Why use Tavily?

Tavily provides research-oriented web search specifically designed for AI applications, enabling retrieval of relevant and trustworthy information.

---

## Why use Groq?

Groq offers extremely fast inference while hosting powerful open-source language models such as **Llama-3.3-70B-Versatile**, making it ideal for responsive AI applications.

---

## Does the application support recent information?

Yes.

Whenever the Query Analysis Agent determines that a query requires up-to-date information, the application automatically performs a live web search before generating the final response.

---

## Is this a Retrieval-Augmented Generation (RAG) project?

No.

This project is an **Agentic AI workflow** that performs conditional web search and response synthesis. It does not use embeddings or a vector database, which are core components of a traditional RAG pipeline.

---

# 🤝 Contributing

Contributions are welcome.

If you would like to improve this project:

1. Fork the repository.
2. Create a new feature branch.
3. Commit your changes.
4. Push the branch.
5. Submit a Pull Request.

Suggestions, feature requests, and improvements are always appreciated.

---

# 📜 License

This project is licensed under the **MIT License**.

You are free to use, modify, and distribute this project for educational and personal purposes.

See the `LICENSE` file for complete details.

---

# 👩‍💻 Author

## Pavithra P N

**Generative AI Enthusiast | AI Developer | Python Programmer**

### Areas of Interest

- Generative AI
- Agentic AI
- Retrieval-Augmented Generation (RAG)
- Large Language Models
- LangGraph
- LangChain
- Artificial Intelligence
- Machine Learning
- Natural Language Processing
- AI Automation
- Data Science

---

# 🙏 Acknowledgements

Special thanks to the developers and open-source communities behind the technologies that made this project possible.

This project is built using:

- LangGraph
- LangChain
- Groq
- Meta AI (Llama Models)
- Tavily Search
- Streamlit
- Python
- Open Source Community

Their contributions continue to advance AI research and application development.

---

# 📌 GitHub Topics

For better repository discoverability, consider adding the following GitHub Topics:

```
generative-ai
agentic-ai
langgraph
langchain
groq
llama
llm
streamlit
python
artificial-intelligence
ai-agent
workflow
tavily
multi-agent
research-assistant
```

---

# ⭐ Support the Project

If you found this project helpful or learned something from it:

⭐ Star the repository

🍴 Fork the repository

📝 Share your feedback

🤝 Contribute to future improvements

Your support encourages continued learning and development of open-source AI projects.

---

# 📬 Contact

If you have questions, suggestions, or would like to collaborate on AI-related projects, feel free to connect through GitHub.

Repository:

```
https://github.com/PavithraPN-01/Agent-lgls-stack
```

---

# 🎉 Conclusion

The **Multi-Agent Research Assistant** demonstrates how modern AI systems can combine reasoning, decision-making, and external knowledge retrieval to generate accurate and context-aware responses.

By integrating **LangGraph**, **Groq's Llama-3.3-70B-Versatile**, **Tavily Search API**, and **Streamlit**, this project showcases a complete Agentic AI workflow that is modular, scalable, explainable, and easy to extend.

The repository reflects practical experience in Generative AI, workflow orchestration, state management, API integration, prompt engineering, and modern AI application development. It serves as a strong portfolio project for students, developers, and AI enthusiasts interested in building intelligent multi-agent systems.

---

<div align="center">

## ⭐ If you found this repository helpful, consider giving it a Star!

### Thank you for visiting this project.

### Happy Coding! 🚀

</div>


---
