import os
import sys
import openai
import textwrap

openai.api_key = os.getenv('OPENAI_API_KEY')

MODEL = "gpt-3.5-turbo"

messages = [{"role": "system", "content": "You are a friendly and helpful assistant."}]

# For sarcastic responses:
# messages = [{"role": "system", "content": "You are sarcastic assistant that reluctantly answers questions with sarcastic responses."}]


def generate_response(prompt):
    messages.append(
        {"role": "user", "content": prompt}
    )
    response = openai.ChatCompletion.create(
        model=MODEL,
        messages = messages,
        max_tokens=300,
    )

    message = response['choices'][0]['message']['content']
    message = textwrap.fill(message, width=60)
    numbered_response = ""
    lines = message.split("\n")
    for i, line in enumerate(lines):
        numbered_response += str(i+1) + ". " + line + "\n"
    return message


def chat_prompts():
    while True:
        endmsg = 'Goodbye! See you next time.'
        user_input = input("You: ")
        if user_input.lower() in ["bye", "goodbye", "end", "stop", "exit"]:
            print("ChatGPT: ",(endmsg))
            sys.exit()
        else:
            prompt = (f"User: {user_input} \nChatGPT: ")
            response = generate_response(prompt)
            print("\nChatGPT:", response)
            print('')
            continue