# AI-customer-support-agent


AI Support Agent
A lightweight, local AI customer support assistant built with Streamlit, LangChain, and Ollama. This agent uses a local knowledge base to provide specific answers to customer inquiries.


Features:

 -Local LLM: llama3 via Ollama.

 -Knowledge-Based: Restricts answers to information provided in knowledge.txt.

 -Memory: Maintains conversation history during the session using   StreamlitChatMessageHistory.

 -Streamlit UI: A clean, chat-based interface for easy interaction.



Workflow:

User Input → Streamlit UI → LangChain Orchestrator → System Prompt + Knowledge Base → Chat History  → Ollama→ AI Response → Streamlit UI (Display)



Prerequisites:

 -Ollama: Install from ollama.com

 -Model: Pull the Llama 3 model:
 


Bash:

pip install streamlit langchain langchain-community langchain-core


File Structure:

agent.py: The main application logic and UI.

knowledge.txt: A text file containing the data the AI uses to answer questions.


How to Run:

Bash
streamlit run agent.py
