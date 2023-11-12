def simple_chatbot():
    print("Hello! I'm your chatbot. You can start chatting or type 'exit' to end the conversation.")

    while True:
        user_input = input("You: ")

        if user_input.lower() == 'exit':
            print("Chatbot: Goodbye!")
            break
        elif 'hello' in user_input.lower() or 'hi' in user_input.lower():
            print("Chatbot: Hi there! How can I help you?")
        elif 'how are you' in user_input.lower():
            print("Chatbot: I'm just a program,but I'm here to assistb you!")
        else:
            print("Chatbot: I;m not sure how to respond to that. Can you ask something else?")

if __name__ == "__main__":
    simple_chatbot()