from langchain_intro.chatbot_2 import review_chain

context = "I had a great stay!"
question = "Did anyone have a positive experience?"

print(review_chain.invoke({"context": context, "question": question}))