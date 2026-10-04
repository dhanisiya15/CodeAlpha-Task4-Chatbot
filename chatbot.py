def chatbot():
    print("🤖 Chatbot: Hello! I am a simple chatbot.")
    print("Type 'bye' to exit.")

    while True:
        user = input("You: ").lower().strip()

        if "hello" in user or "hi" in user:
            print("🤖 Chatbot: Hi! Nice to meet you.")

        elif "how are you" in user:
            print("🤖 Chatbot: I'm fine, thanks!")

        elif "your name" in user:
            print("🤖 Chatbot: I am a Python chatbot.")

        elif "thank" in user:
            print("🤖 Chatbot: You're welcome!")

        elif "bye" in user or "goodbye" in user:
            print("🤖 Chatbot: Goodbye! Have a nice day!")
            break

        else:
            print("🤖 Chatbot: Sorry, I don't understand.")


chatbot()