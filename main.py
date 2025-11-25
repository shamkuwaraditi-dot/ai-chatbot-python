import random

responses = {
    "hi": ["Hello!", "Hi there!", "Hey!"],
    "hello": ["Hello!", "Hi!"],
    "how are you": ["I'm doing great!", "I'm fine, thanks!", "All good!"],
    "bye": ["Goodbye!", "See you soon!", "Bye!"]
}

def get_response(user_message):
    user_message = user_message.lower()
    for key in responses:
        if key in user_message:
            return random.choice(responses[key])
    return "Sorry, I don't understand that."

print("AI Chatbot Started. Type 'bye' to exit.")
while True:
    user = input("You: ")
    if user.lower() == "bye":
        print("Bot: Goodbye!")
        break
    print("Bot:", get_response(user))

