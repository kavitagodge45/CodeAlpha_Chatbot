def my_chatbot():
    print("🤖 Hello! I'm your chatbot. Type 'bye' to exit.")

    while True:
        user_input = input("You: ").lower()

        if user_input == "hello":
            print("Bot: Hi there! 😊")

        elif user_input == "how are you":
            print("Bot: I'm doing great! What about you?")

        elif user_input == "your name":
            print("Bot: I'm a simple Python chatbot 🤖")

        elif user_input == "bye":
            print("Bot: Goodbye! Have a nice day 👋")
            break

        else:
            print("Bot: Sorry, I didn't understand that.")

my_chatbot()
