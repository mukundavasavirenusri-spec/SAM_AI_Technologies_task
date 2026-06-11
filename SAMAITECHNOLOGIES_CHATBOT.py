def chatbot():
    print("Simple Chatbot (type 'bye' to exit)\n")

    while True:
        user_input = input("You: ").lower().strip()

        if user_input == "bye":
            print("Bot: Goodbye!")
            break

        elif "hello" in user_input or "hi" in user_input:
            print("Bot: Hello! How can I help you?")

        elif "how are you" in user_input:
            print("Bot: I'm doing well. Thanks for asking!")

        elif "your name" in user_input:
            print("Bot: I'm a simple Python chatbot.")

        elif "help" in user_input:
            print("Bot: I can respond to greetings and simple questions.")

        else:
            print("Bot: Sorry, I don't understand that.")

if __name__ == "__main__":
    chatbot()