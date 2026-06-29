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

The **Multi-Agent Research Assistant** is an intelligent **Agentic AI application** that demonstrates how multiple AI agents can collaborate to solve user queries efficiently.

Unlike traditional chatbots that answer every question using only a Large Language Model (LLM), this project introduces an intelligent decision-making workflow powered by **LangGraph**.

The system first analyzes the user's question and determines whether it can answer using the LLM's internal knowledge or whether it should retrieve the latest information from the internet using the **Tavily Search API**.

If recent or dynamic information is required, the application performs a live web search, gathers relevant information from trusted sources, and synthesizes a comprehensive response.

If the query is general knowledge, the system directly generates an answer using the Groq-hosted Llama 3.3 model without performing unnecessary searches.

This project demonstrates the practical implementation of **Agentic AI**, where multiple specialized agents work together to provide accurate, efficient, and context-aware responses.

---

# 🎯 Problem Statement

Large Language Models possess extensive knowledge but are limited by the data on which they were trained.

They cannot reliably answer:

- Latest news
- Recent technological advancements
- Current affairs
- Live market information
- Updated research publications

On the other hand, searching the internet for every question introduces unnecessary latency, API costs, and computational overhead.

This project addresses these challenges by implementing an intelligent decision-making agent capable of determining when external information is actually required.

The result is a faster, smarter, and more efficient AI assistant.

---

# 💡 Motivation

The inspiration behind this project was to understand how modern AI systems such as ChatGPT, Claude, Gemini, and Perplexity intelligently decide between internal reasoning and external knowledge retrieval.

Instead of building a simple chatbot, this project focuses on developing an **Agentic AI Workflow** capable of:

- Making autonomous decisions
- Executing multiple tasks
- Managing workflow states
- Collaborating between specialized agents
- Producing reliable and explainable responses

---

# ✨ Key Features

## 🤖 Intelligent Query Analysis

- Determines whether the user's question requires live web search.
- Reduces unnecessary API usage.
- Improves overall response time.

---

## 🌐 Live Web Search

- Integrated with Tavily Search API.
- Retrieves trusted and relevant sources.
- Supports research-oriented queries.

---

## 🧠 Direct Knowledge Answering

- Uses Groq's Llama 3.3 70B Versatile model.
- Answers general knowledge questions instantly.
- Eliminates unnecessary internet requests.

---

## 🔀 Conditional Workflow Routing

Implemented using LangGraph.

The workflow dynamically changes depending on the query type.

Example:

General Question

```
User Question

↓

Analyze

↓

Direct Answer

↓

End
```

Research Question

```
User Question

↓

Analyze

↓

Web Search

↓

Synthesis

↓

Final Answer

↓

End
```

---

## 📊 Step-by-Step Agent Tracking

The application displays every action taken by the agent.

Example:

```
🧠 Analyze Query

↓

🌐 Search Internet

↓

✍️ Generate Final Response
```

This provides transparency and helps users understand how the system reached its final answer.

---

## 🎨 Interactive User Interface

Built using Streamlit.

Features include:

- Clean dashboard
- Sidebar configuration
- Secure API key entry
- Interactive status updates
- Expandable search results
- Markdown formatted responses

---

# 🏗️ System Architecture

```
                User Query
                     │
                     ▼
        ┌────────────────────────┐
        │   Analyze Agent        │
        └────────────────────────┘
                     │
      ┌──────────────┴──────────────┐
      │                             │
      ▼                             ▼
Needs Web Search?              Direct Answer
      │                             │
      ▼                             ▼
┌────────────────┐          ┌────────────────┐
│ Tavily Search  │          │ Groq LLM       │
└────────────────┘          └────────────────┘
      │
      ▼
┌────────────────┐
│ Synthesis Node │
└────────────────┘
      │
      ▼
 Final Response
```

---

# 🧠 Agent Workflow

The application consists of four intelligent AI agents working collaboratively.

---

## Agent 1 – Query Analyzer

### Purpose

The Query Analyzer is responsible for understanding the user's request.

### Responsibilities

- Analyze the query
- Determine whether external knowledge is required
- Route the workflow

### Example

Input

```
What is Python?
```

Decision

```
DIRECT
```

---

Input

```
Latest AI News
```

Decision

```
SEARCH
```

---

## Agent 2 – Web Search Agent

This agent is only activated when the analyzer determines that recent information is required.

Responsibilities:

- Perform web search
- Retrieve top sources
- Organize retrieved content
- Pass information to the synthesis agent

Search Engine Used

- Tavily Search API

Maximum Search Results

```
3 Sources
```

---

## Agent 3 – Synthesis Agent

After retrieving information, this agent generates a comprehensive response.

Responsibilities

- Read retrieved documents
- Remove duplicate information
- Generate a coherent summary
- Produce a natural language response
- Preserve important facts

---

## Agent 4 – Direct Answer Agent

This agent handles general knowledge questions.

Responsibilities

- Query Groq Llama 3.3
- Generate concise responses
- Skip unnecessary searches
- Reduce latency

```

---

# 🛠️ Technology Stack

The project is built using modern Generative AI frameworks and tools that enable intelligent workflow orchestration, natural language understanding, and live web information retrieval.

| Technology | Purpose |
|------------|---------|
| **Python 3.11+** | Core programming language |
| **LangGraph** | Multi-agent workflow orchestration |
| **LangChain** | LLM integration framework |
| **Groq API** | High-speed LLM inference |
| **Llama 3.3 70B Versatile** | Large Language Model |
| **Tavily Search API** | Live web search and retrieval |
| **Streamlit** | Interactive web application |
| **python-dotenv** | Environment variable management |
| **Typing** | State type definitions |
| **Operator** | State aggregation |

---

# 📂 Project Structure

```
Multi-Agent-Research-Assistant/
│
├── agentic-app.py
├── main.py
├── requirements.txt
├── .env
├── .gitignore
├── README.md
│
├── Tests_Scriptfiles/
│   ├── tavily-connection.py
│   ├── groq-test.py
│   └── other utility scripts
│
├── screenshots/
│   ├── home.png
│   ├── workflow.png
│   ├── answer.png
│   └── search-results.png
│
└── assets/
    └── architecture.png
```

---

# 📁 File Description

## 📌 agentic-app.py

This is the main Streamlit application.

Responsibilities include:

- Creating the web interface
- Accepting user queries
- Collecting API keys
- Executing the LangGraph workflow
- Displaying reasoning steps
- Presenting the final answer
- Showing raw search results

This file acts as the frontend of the application.

---

## 📌 main.py

This file contains the core business logic.

It defines:

- ResearchState
- LangGraph workflow
- Agent Nodes
- Routing Logic
- Search Integration
- Answer Generation

This is the heart of the application where all AI reasoning takes place.

---

## 📌 requirements.txt

Contains all Python dependencies required for running the project.

Example packages include:

- streamlit
- langgraph
- langchain
- langchain-groq
- tavily-python
- python-dotenv

---

## 📌 .env

Stores secret API credentials.

Example

```text
groq_api_key=YOUR_GROQ_API_KEY

tavily_api_key=YOUR_TAVILY_API_KEY
```

This file is ignored by Git using `.gitignore`.

---

# 🧠 LangGraph State Management

The workflow maintains a shared state throughout execution.

The state contains:

| Variable | Description |
|-----------|-------------|
| query | User question |
| needs_search | Decision made by analyzer |
| search_results | Retrieved web information |
| final_answer | Generated response |
| steps | Workflow execution history |

The state is continuously updated as different agents complete their tasks.

---

# 🔄 Workflow Execution

The LangGraph workflow executes in the following sequence.

```
START

↓

Analyze Query

↓

Does it need Search?

↓

YES ───────────────► Search Web

│                       │

│                       ▼

│               Retrieve Sources

│                       │

│                       ▼

│                Synthesize Answer

│                       │

│                       ▼

└──────────────► Final Response

NO

↓

Direct Answer

↓

Final Response

↓

END
```

---

# 🔀 Conditional Routing

One of the most important features of this project is dynamic routing.

Instead of following a fixed pipeline, the workflow changes depending on user intent.

For example,

Question:

```
Explain Neural Networks
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

Question

```
Latest AI regulations in Europe
```

Workflow

```
Analyze

↓

Search

↓

Synthesize

↓

End
```

This significantly improves efficiency.

---

# 🌐 Live Web Search

Whenever recent information is required, the application uses the Tavily Search API.

The retrieved sources are:

- High quality
- Research focused
- Relevant to the query

The search results are passed directly to the synthesis agent.

---

# 🤖 Large Language Model

The application uses

## Groq

Model

```
Llama-3.3-70B-Versatile
```

Reasons for choosing this model:

- High reasoning capability
- Fast inference
- Strong instruction following
- Excellent summarization
- Low latency

---

# 🎨 User Interface

The Streamlit application provides an intuitive interface.

Features include:

- Query input box
- Sidebar API configuration
- Workflow progress tracker
- Final answer section
- Expandable search results
- Interactive execution status

---

# 🚀 Installation Guide

## Step 1

Clone the repository.

```bash
git clone https://github.com/PavithraPN-01/Agent-lgls-stack.git

cd Agent-lgls-stack
```

---

## Step 2

Create a virtual environment.

Windows

```bash
python -m venv venv
```

Activate

```bash
venv\Scripts\activate
```

Linux / macOS

```bash
python3 -m venv venv

source venv/bin/activate
```

---

## Step 3

Install dependencies.

```bash
pip install -r requirements.txt
```

---

## Step 4

Create a `.env` file.

```text
groq_api_key=YOUR_GROQ_API_KEY

tavily_api_key=YOUR_TAVILY_API_KEY
```

---

## Step 5

Run the application.

```bash
streamlit run agentic-app.py
```

The application will launch automatically in your browser.

---

# 🔑 API Keys Required

This project requires two API keys.

## 1. Groq API

Used for

- Query analysis
- Direct answering
- Response synthesis

---

## 2. Tavily API

Used for

- Live internet search
- Research retrieval
- Recent information

---

# 💬 Example Queries

General Knowledge

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

Current Affairs

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

Programming

```
Explain LangGraph.
```

Expected Workflow

```
Direct Answer
```

---

Research

```
Recent developments in Quantum Computing
```

Expected Workflow

```
Analyze

↓

Search

↓

Final Answer
```

---

# 📊 Sample Output

```
🧠 Decision: Web Search

🌐 Retrieved 3 Sources

✍️ Generated Final Answer

---------------------------------

Final Answer:

Large Language Models have recently...
```


---

# 🧪 Testing

The application has been tested using different categories of queries.

✔ General Knowledge

✔ Programming

✔ Research

✔ Current Affairs

✔ Technology

✔ Science

✔ AI & Machine Learning

✔ Latest News

✔ Educational Questions

✔ Web Search Queries

---

# 🌟 Project Highlights

This project demonstrates the practical implementation of **Agentic AI** using a graph-based workflow. Instead of relying solely on a Large Language Model (LLM), the application intelligently decides whether to answer from internal knowledge or retrieve real-time information from the web.

### Key Highlights

- 🤖 Multi-Agent AI Workflow
- 🔄 Conditional Routing using LangGraph
- 🌐 Live Web Search Integration
- 🧠 Intelligent Decision Making
- ⚡ High-Speed Inference using Groq
- 📚 Research-Oriented Responses
- 🎨 Interactive Streamlit Dashboard
- 🔐 Secure API Key Management
- 📊 Transparent Agent Execution
- 📝 Well-Structured Response Generation

---

# 📚 Concepts Demonstrated

This project showcases knowledge and practical implementation of:

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
- AI Application Deployment

---

# 🎯 Skills Demonstrated

Through this project, the following technical skills have been applied:

### Programming Skills

- Python Programming
- Object-Oriented Programming
- Modular Code Organization

### Artificial Intelligence

- Large Language Models
- Agentic AI
- AI Workflow Design
- Prompt Engineering
- Information Retrieval

### Frameworks

- LangGraph
- LangChain
- Streamlit

### APIs

- Groq API
- Tavily Search API

### Software Engineering

- State Management
- Clean Code
- Modular Architecture
- Environment Configuration
- Error Handling
- Git & GitHub

---

# 🎓 Learning Outcomes

This project helped in understanding:

- How AI Agents communicate with each other.
- How LangGraph manages workflow execution.
- How state is passed between multiple agents.
- How to integrate external tools into AI applications.
- How LLMs can make autonomous decisions.
- How to build production-ready AI applications.
- How to design explainable AI systems.
- How to create scalable multi-agent workflows.

---

# 🚧 Challenges Faced

During development, several challenges were encountered:

- Understanding LangGraph workflow execution
- Managing shared application state
- Designing effective prompts for routing decisions
- Integrating multiple APIs
- Handling environment variables securely
- Creating a modular project structure
- Building a responsive user interface
- Debugging workflow transitions
- Improving answer quality
- Reducing unnecessary API calls

Each challenge provided valuable experience in building real-world AI systems.

---

# 🚀 Future Enhancements

This project serves as a foundation for more advanced Agentic AI systems.

Future improvements include:

- 💬 Multi-turn conversation memory
- 🧠 Long-term memory using vector databases
- 📄 PDF and document analysis
- 📚 Retrieval-Augmented Generation (RAG)
- 🗂️ FAISS or ChromaDB integration
- 🖼️ Image understanding using multimodal models
- 🎙️ Voice-based interaction
- 🌍 Multi-language support
- 📊 Analytics Dashboard
- 📈 Agent Performance Monitoring
- 🔍 Citation-based responses
- 🧩 Multi-agent collaboration with additional specialized agents
- ☁️ Cloud deployment
- 🐳 Docker containerization
- 🔐 User authentication and session management

---

# ⚡ Performance Considerations

The application has been designed to optimize both response quality and execution speed.

Performance strategies include:

- Conditional routing to avoid unnecessary web searches
- High-speed Groq inference
- Lightweight Streamlit interface
- Efficient state management using LangGraph
- Limited search results for faster synthesis
- Modular workflow execution

---

# 🔒 Security Practices

Security has been considered throughout development.

Implemented practices include:

- API keys stored in environment variables
- `.env` excluded using `.gitignore`
- No hardcoded credentials
- Secure API key input through Streamlit sidebar
- Local execution of sensitive configuration

---

# 📖 Frequently Asked Questions (FAQ)

### Why use LangGraph instead of a simple LLM?

LangGraph enables conditional workflows, allowing the application to make intelligent decisions about which actions to perform instead of following a fixed sequence.

---

### Why use Tavily?

Tavily is specifically designed for AI applications and provides high-quality, research-oriented search results.

---

### Why use Groq?

Groq offers extremely fast inference while supporting advanced open-source language models such as Llama 3.3.

---

### Does this project support recent information?

Yes.

Whenever the analyzer determines that a query requires up-to-date information, the system automatically performs a live web search.

---

### Is this a Retrieval-Augmented Generation (RAG) system?

No.

This project is an **Agentic AI application** that performs conditional web search and response synthesis. It does not use embeddings or a vector database, which are core components of a traditional RAG pipeline.

---

# 🤝 Contributing

Contributions are welcome.

If you would like to improve this project:

1. Fork the repository
2. Create a new feature branch
3. Commit your changes
4. Push the branch
5. Open a Pull Request

Suggestions, feature requests, and improvements are always appreciated.

---

# 📜 License

This project is licensed under the **MIT License**.

You are free to use, modify, and distribute this project for educational and personal purposes.

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

Special thanks to the open-source AI community and the creators of the amazing technologies used in this project.

This project would not have been possible without:

- LangGraph
- LangChain
- Groq
- Meta AI (Llama Models)
- Tavily Search
- Streamlit
- Python Community
- Open Source Contributors

---

# 📌 GitHub Topics

To improve repository discoverability, add the following GitHub Topics:

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

If you found this project useful or learned something from it:

⭐ Star the repository

🍴 Fork the repository

📝 Share your feedback

🤝 Contribute to the project

Your support helps improve the project and motivates further development.

---

# 📬 Contact

If you have questions, suggestions, or would like to collaborate on AI-related projects, feel free to connect through GitHub.

Repository:

```
https://github.com/PavithraPN-01/Agent-lgls-stack
```

---

# 🎉 Conclusion

The **Multi-Agent Research Assistant** demonstrates how modern AI systems can intelligently combine reasoning, decision-making, and external knowledge retrieval to deliver accurate and context-aware responses.

By integrating **LangGraph**, **Groq's Llama 3.3**, **Tavily Search API**, and **Streamlit**, this project showcases a complete Agentic AI workflow that is modular, scalable, and production-ready.

This project reflects practical skills in Generative AI, workflow orchestration, state management, API integration, and modern AI application development, making it a strong portfolio project for anyone exploring Agentic AI systems.

---

<div align="center">

### ⭐ If you found this repository helpful, consider giving it a star!

**Thank you for visiting this project! Happy Coding! 🚀**

</div>
