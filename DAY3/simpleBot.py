import ollama
while True:
    question = input("Enter your question: ")
    if question.lower() == "exit":
        break
    response = ollama.chat(
        model = "llama3.2:3b",
        messages = [
            {
                "role": "user",
                "content": "Give the answers in 2 lines only"
            },
            {
                "role": "user",
                "content": question
            }
        ]
    )
    print(response["message"]["content"])
