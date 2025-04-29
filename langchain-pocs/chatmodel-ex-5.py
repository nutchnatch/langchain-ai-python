from langchain_intro.chatbot_3 import review_chain

question = """Has anyone complained about
...            communication with the hospital staff?"""

print(review_chain.invoke(question))