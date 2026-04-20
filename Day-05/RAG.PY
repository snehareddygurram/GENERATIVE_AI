import requests

# Load your data
with open("Day-05/data.txt", "r") as file:
    context = file.read()

print("🤖 RAG Chatbot (type 'exit' to stop)\n")

while True:
    question = input("You: ")

    if question.lower() == "exit":
        break

    prompt = f"""
    Answer ONLY from the context below.

    Context:
    {context}

    Question:
    {question}
    """

    response = requests.post(
        "http://localhost:11434/api/generate",
        json={
            "model": "llama3.1:8b",
            "prompt": prompt,
            "stream": False
        }
    )

    data = response.json()
    print("Bot:", data.get("response", "No response"))
    print("-" * 40)