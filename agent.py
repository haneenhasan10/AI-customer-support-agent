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
llm = Ollama(model = 'llama3')

with open("knowledge.txt", "r") as f:
    knowledge_base = f.read()

# builed the prompt 
prompt = ChatPromptTemplate.from_messages([
    ("system", f"You are a professional customer support assistant.dont take side conversation,  Answer only based on the following information: \n{knowledge_base}"),
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