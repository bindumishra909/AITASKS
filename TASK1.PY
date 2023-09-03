import re

# Define predefined rules and responses
rules = {
    r'hello|hi|hey|greetings': 'Hello! How can I assist you today?',
    r'how are you|how are you doing': 'I am just a computer program, but thanks for asking!',
    r'what is your name|who are you': "I'm is a robot. You can call me robot.",
    r'bye|goodbye|exit': 'Goodbye! Feel free to return if you have more questions.',
}

# Function to match user input to predefined rules
def match_rule(user_input, rules):
    for pattern, response in rules.items():
        if re.search(pattern, user_input, re.IGNORECASE):
            return response
    return "I'm sorry, I don't understand that question."

# Main loop to handle user interactions
while True:
    user_input = input("You: ").strip()
    if user_input.lower() == 'exit':
        print("Chatbot: Goodbye!")
        break
    response = match_rule(user_input, rules)
    print("Chatbot:", response)
