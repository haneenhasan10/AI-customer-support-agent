from langchain_community.llms import Ollama


llm = Ollama(model = 'llama3')
knowledge = open("knowledge.txt").read()

def ask_agent(question):

    prompt = f"""
    You are a customer support AI agent.
    Only answer using the information in the knowledge base.
    If the information is not available, say you don't know..
    Use this information to answer the question.

    Knowledge:
    {knowledge}

    Question:
    {question}
    """

    response = llm.invoke(prompt)

    return response


while True:
    q = input("Ask a question: ")
    answer = ask_agent(q)
    print("Agent:", answer)