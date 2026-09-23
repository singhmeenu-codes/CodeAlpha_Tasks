"""
Basic Rule-Based Chatbot
-------------------------
A simple chatbot that matches user input against predefined patterns and replies accordingly, using if-elif logic.

Key Concepts Used: if-elif, functions, loops, input/output.
"""

# Predefined keyword -> reply pairs.
# Each entry is a list of keywords that should trigger the same reply.
RESPONSES = [
    (["hello", "hi", "hey"], "Hi there! How can I help you today?"),
    (["how are you", "how're you", "how are u"], "I'm fine, thanks! How about you?"),
    (["your name", "who are you"], "I'm a simple rule-based chatbot."),
    (["what can you do", "help"], "I can chat about a few basic things — try saying hello, "
                                    "asking how I am, or asking my name."),
    (["thank you", "thanks"], "You're welcome!"),
]

EXIT_KEYWORDS = ["bye", "goodbye", "exit", "quit"]


def get_response(user_input):
    """
    Check the user's message against known keyword patterns
    and return the matching reply. Falls back to a default
    response if nothing matches.
    """
    message = user_input.lower().strip()

    # Check for exit keywords first
    for word in EXIT_KEYWORDS:
        if word in message:
            return "Goodbye!"

    # Check each predefined pattern group
    for keywords, reply in RESPONSES:
        for keyword in keywords:
            if keyword in message:
                return reply

    # Default fallback if nothing matched
    return "Sorry, I didn't understand that. Could you rephrase?"


def is_exit(user_input):
    """Return True if the message contains an exit keyword."""
    message = user_input.lower().strip()
    return any(word in message for word in EXIT_KEYWORDS)


def chat():
    print("Chatbot: Hi! I'm a simple chatbot. Type 'bye' to end our chat.\n")

    while True:
        user_input = input("You: ").strip()

        if not user_input:
            print("Chatbot: Please type something.\n")
            continue

        response = get_response(user_input)
        print(f"Chatbot: {response}\n")

        if is_exit(user_input):
            break


if __name__ == "__main__":
    chat()