import requests

response = requests.post(
    "http://localhost:11434/api/generate",
    json={
        "model": "llama3.1:8b",
        "prompt": "Explain AI in simple words",
        "stream": False
    }
)

data = response.json()
print(data.get("response", "No response found"))