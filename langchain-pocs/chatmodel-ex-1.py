from langchain.schema.messages import HumanMessage, SystemMessage
from langchain_intro.chatbot import chat_model

messages = [
     SystemMessage(
         content="""You're an assistant knowledgeable about
         healthcare. Only answer healthcare-related questions."""
     ),
    #HumanMessage(content="What is Medicaid managed care?"),
     HumanMessage(content="How do I change a tire?"),
 ]

print(chat_model.invoke(messages))