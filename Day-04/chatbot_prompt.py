import requests

print("🤖 Smart AI Chatbot (type 'exit' to stop)\n")

while True:
    user_input = input("You: ")

    if user_input.lower() == "exit":
        print("Bot: Bye 👋")
        break

    prompt = f"""
    You are a helpful AI tutor.
    Answer clearly and simply.
    Use bullet points if possible.

    Question: {user_input}
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
    print("Bot:\n", data.get("response", "No response"))
    print("-" * 50)