import requests

# Load data
with open("Day-06/data.txt", "r") as f:
    data = f.readlines()

print("🤖 Vector RAG (type exit to stop)\n")

while True:
    question = input("You: ")

    if question.lower() == "exit":
        break

    # Simple search (keyword match)
    relevant = ""
    for line in data:
        if any(word.lower() in line.lower() for word in question.split()):
            relevant += line

    prompt = f"""
    Answer using only this context:

    {relevant}

    Question: {question}
    """

    response = requests.post(
        "http://localhost:11434/api/generate",
        json={
            "model": "llama3.1:8b",
            "prompt": prompt,
            "stream": False
        }
    )

    result = response.json()
    print("Bot:", result.get("response", "No answer"))
    print("-" * 40)