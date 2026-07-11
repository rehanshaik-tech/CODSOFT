# Rule-Based Chatbot
print("===================================")
print("      SIMPLE RULE-BASED CHATBOT")
print("Type 'bye' to exit the chatbot.")
print("===================================")

while True:
    user = input("\nYou: ").lower().strip()

    if user == "bye":
        print("Bot: Goodbye! Have a wonderful day.")
        break

    elif "hello" in user or "hi" in user:
        print("Bot: Hello! Nice to meet you.")

    elif "how are you" in user:
        print("Bot: I'm doing great. Thanks for asking!")

    elif "your name" in user:
        print("Bot: My name is SmartBot.")

    elif "time" in user:
        from datetime import datetime
        print("Bot: Current time is", datetime.now().strftime("%I:%M %p"))

    elif "date" in user:
        from datetime import datetime
        print("Bot: Today's date is", datetime.now().strftime("%d-%m-%Y"))

    elif "thank" in user:
        print("Bot: You're welcome!")

    elif "help" in user:
        print("Bot: You can ask me about my name, date, time, or greet me.")

    else:
        print("Bot: Sorry, I don't understand that. Please try another question.")