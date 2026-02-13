from groq import Groq
GROQ_API_KEY="API_KEY"
client=Groq(api_key=GROQ_API_KEY)

data = [
    "Python is a programming language.",
    "Java is used for application development.",
    "HTML means Hyper Text Markup Language.",
    "CSS means Cascading Style Sheet.",
    "ML is a part of AI."
    ]

def get_context(question):
    question=question.lower()
    for line in data:
        for word in question.split():
            if word in line.lower():
                return line
    return None
def chatbot(question):
    context=get_context(question)
    if not context:
        return "I don't know the answer"
    
    response=client.chat.completions.create(
        model="llama-3.1-8b-instant",
        messages=[
            {"role":"system","content":"Answer only using the given context."},
            {"role":"user","content":f"Context:{context}\nQuestion:{question}"}
        ],
        temperature=0.7
    )
    return response.choices[0].message.content
print("General Q/A Chatbot(type exit to quit)\n")

while True:
    q=input("You:" )
    if q.lower()=="exit":
        break
    print("Bot:",chatbot(q))






