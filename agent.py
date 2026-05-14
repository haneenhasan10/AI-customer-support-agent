import streamlit as st
from langchain_community.llms import Ollama
from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder
from langchain_community.chat_message_histories import StreamlitChatMessageHistory
from langchain_core.runnables.history import RunnableWithMessageHistory

# user interface 
st.set_page_config(page_title=('AI support agent'))
st.title('AI support agent')

# use StreamlitChatMessageHistory to store current conversation 
msgs = StreamlitChatMessageHistory(key = 'special_app_key')

# load the model  
llm = Ollama(model = 'llama3',
             base_url="http://host.docker.internal:11434")

with open("knowledge.txt", "r") as f:
    knowledge_base = f.read()

# builed the prompt 

system_instruction =  f"""
You are the official Virtual Assistant for (Haneen Company). Your sole mission is to assist customers strictly based on the provided "Official Knowledge Base" below.

You must follow these strict operational rules:
1. Concise Responses: Answer questions directly, accurately, and politely. Avoid any unnecessary chitchat, small talk, or overly lengthy explanations.
2. Strict Factuality: Do not invent, guess, or assume any information not explicitly mentioned in the Knowledge Base. 
3. Handling Missing Information: If a customer asks about something NOT covered in the Knowledge Base (e.g., specific product prices, Cash on Delivery, or a return request after 7 days), you must politely but firmly reply: "I apologize, but I do not have this information available at the moment. Please contact our technical support at support@haneen.com for further assistance."
4. Stay in Context: If the customer tries to discuss topics outside of Haneen Company's scope (e.g., weather, coding, or politics), politely redirect them by saying: "I am only authorized to assist you with inquiries regarding Haneen Company."
5. Language: Always respond in the same language the customer uses to greet or ask you (e.g., if they ask in Arabic, reply in Arabic, but strictly follow these English guidelines).

Official Knowledge Base:
{knowledge_base}
"""

prompt = ChatPromptTemplate.from_messages([
    ("system",system_instruction),
    MessagesPlaceholder(variable_name="history"),
    ("human", "{question}"),
])

# link the model with  memory and  prompt
chain = prompt | llm
chain_with_history = RunnableWithMessageHistory(
    chain,
    lambda session_id: msgs,
    input_messages_key="question",
    history_messages_key="history",
)

# display previous messages on the screen
for msg in msgs.messages:
    st.chat_message(msg.type).write(msg.content)

# take user's input and process it
if question := st.chat_input("How can I help you"):
    st.chat_message("human").write(question)
    
    with st.spinner('Thinking'):
        # send the question to the model
        response = chain_with_history.invoke(
            {"question": question},
            config={"configurable": {"session_id": "any"}}
        )
        st.chat_message("ai").write(response)