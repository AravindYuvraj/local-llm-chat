import requests

prompt = "What is the capital of India?"

response = requests.post(
    'http://localhost:11434/api/generate',
    json={
        'model': 'llama3',
        'prompt': prompt,
        'stream': False  # 🛠️ Important: disable streaming to get full JSON
    }
)

data = response.json()

print(f"Prompt: {prompt}")
print(f"AI Response: {data['response']}")
