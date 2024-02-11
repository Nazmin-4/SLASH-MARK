import nltk
from nltk.chat.util import Chat, reflections

# Define pairs of patterns and responses for the chatbot
pairs = [
    [
        r"my name is (.*)",
        ["Hello %1, how can I help you today?",]
    ],
    [
        r"what is your name?",
        ["My name is Chatbot and I'm here to assist you.",]
    ],
    [
        r"how are you?",
        ["I'm doing well, thank you!", "I'm feeling great, thanks for asking.",]
    ],
    [
        r"(.*) your name?",
        ["My name is Chatbot and I'm here to assist you.",]
    ],
    [
        r"quit",
        ["Bye! Take care. See you soon.",]
    ],
]


chatbot = Chat(pairs, reflections)

def main():
    print("Welcome! How can I assist you today?")
    while True:
        user_input = input("> ")
        response = chatbot.respond(user_input)
        print(response)
        if user_input.lower() == "quit":
            break

if __name__ == "__main__":
    main()
