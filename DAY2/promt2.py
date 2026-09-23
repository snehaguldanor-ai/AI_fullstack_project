import ollama
response = ollama.chat(
    model = "llama3.2:3b",
    messages = [
        {
            "role": "user",
            "content": "what is AI? what are types of ai and explain them in the 50 words"
        }
    ]
)
print(response["message"]["content"])