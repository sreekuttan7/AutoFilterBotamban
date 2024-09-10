
# Importing necessary libraries
from nltk.chat.util import Chat, reflections

pairs = [
    [
        r"my name is (.*)",
        ["Hello %1, how can I help you today?",]
    ],
    [
        r"(.*) (good|fine)",
        ["That's great to hear. How can I assist you?",]
    ],
    [
        r"(.*) (help|support)",
        ["Sure, I can help you. What do you need assistance with?",]
    ],
    [
        r"quit",
        ["Thank you for chatting with me. Have a great day!"]
    ],
    [
        r'(.*)',
        ["Sorry, I did not understand that. Can you please rephrase it?",]
    ]
]

def chatbot():
    print("Hello, I'm a simple chatbot. How can I assist you today? Type 'quit' to exit.")
    chat = Chat(pairs, reflections)
    while True:
        user_input = input("User: ")
        response = chat.respond(user_input)
        print("ChatBot:", response)
        if user_input == 'quit':
            break

if __name__ == "__main__":
    chatbot()
