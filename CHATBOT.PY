# Rule-Based Chatbot
# Internship Task 1

print("===================================")
print("      Simple Rule-Based Chatbot")
print("===================================")

name = input("Enter your name: ")
print(f"\nHello {name}! I am ChatBot.")
print("Type 'bye' to end the conversation.\n")

while True:
    user = input("You: ").lower().strip()

    if user == "hello" or user == "hi":
        print("Bot: Hello! Nice to meet you.")

    elif "how are you" in user:
        print("Bot: I'm doing great! Thanks for asking.")

    elif "your name" in user:
        print("Bot: My name is ChatBot.")

    elif "help" in user:
        print("Bot: I can answer simple questions like greetings, time, date, and your name.")

    elif "time" in user:
        from datetime import datetime
        print("Bot: Current time is", datetime.now().strftime("%I:%M %p"))

    elif "date" in user:
        from datetime import datetime
        print("Bot: Today's date is", datetime.now().strftime("%d-%m-%Y"))

    elif "thank" in user:
        print("Bot: You're welcome!")

    elif "bye" in user:
        print(f"Bot: Goodbye {name}! Have a wonderful day.")
        break

    else:
        print("Bot: Sorry, I don't understand that. Please try another question.")