import ollama
response = ollama.chat(
    model = "llama3.2:3b",
    messages = [
        {
            "role": "user",
                        "content": "Give the answers in child understandable way in 2 lines only"
        },
        {
            "role": "user",
            "content": "explain ai"
        }
    ]
)
print(response["message"]["content"])