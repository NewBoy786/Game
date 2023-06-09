import openai

# Set up your OpenAI API key
openai.api_key = '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'

# Define a function to interact with the chatbot
def chat_with_bot(message):
    response = openai.Completion.create(
        engine='text-davinci-003',
        prompt=message,
        temperature=0.7,
        max_tokens=100,
        n=1,
        stop=None,
    )
    return response.choices[0].text.strip()

# Main loop to chat with the bot
print("Welcome to the Mental Health Chatbot!")
print("You can start chatting by typing your message. Enter 'exit' to quit.")

while True:
    user_input = input("User: ")
    if user_input.lower() == 'exit':
        break

    # Prepend a system message to the user's input
    chat_history = 'User: ' + user_input + '\nBot: '

    # Generate bot's response
    bot_response = chat_with_bot(chat_history)

    print("Bot:", bot_response)
    print("Bot:", bot_response)
