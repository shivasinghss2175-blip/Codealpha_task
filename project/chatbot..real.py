


def chatbot():
    print(" Chatbot: Hello! Welcome to my chatbot.")
    print("Type 'bye' to exit the conversation.")

    while True:
        # Take user input and convert it into lowercase
        user_input = input("You: ").lower().strip()

        if user_input == "hello":
            print("Bot: Hi! Nice to meet you.")

        elif user_input == "how are you":
            print("Bot: I'm fine, thanks! How are you?")

        elif user_input == "what is your name":
            print("Bot: I'm a simple Python chatbot.")

        elif user_input == "what can you do":
            print("Bot: I can chat with you and answer simple messages.")

        elif user_input == "bye":
            print("Bot: Goodbye! Have a great day!")
            break  # Stop the loop and end the conversation

        else:
            print("Bot: Sorry, I don't understand that.")

chatbot()  # Call the function to start the chatbot
        
