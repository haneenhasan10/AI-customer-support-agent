# AI-customer-support-agent


AI customer support assistant built with Streamlit, LangChain, and Ollama. The  application is containerized using **Docker** for consistent environment deployment.



## Features
* **Strict Context Enforcement:** The agent strictly answers based on the provided `knowledge.txt` and refuses to hallucinate or talk out of scope.
* **Session Memory:** Retains conversation history during the user session using `StreamlitChatMessageHistory`.
* **Dockerized Environment:** Isolated and clean setup, eliminating the "it works on my machine" issue.
* **Local LLM Integration:** Communicates seamlessly from inside the Docker container to the host machine's Ollama instance.

---

## Tech Stack
* **Frontend:** Streamlit
* **LLM Orchestration:** LangChain (Core & Community)
* **Local LLM Server:** Ollama (Llama 3)
* **Containerization:** Docker

---

##  Project Structure
```text
├── agent.py              # Main application logic & Streamlit UI
├── Dockerfile            # Docker configuration recipe
├── requirements.txt      # Python dependencies
├── knowledge.txt         # The company's official knowledge base
└── README.md             # Project documentation

