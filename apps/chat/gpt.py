import os
import sys
from dotenv import load_dotenv
import openai
load_dotenv('./.env')
import textwrap

openai.api_key = os.environ['OPENAI_API_KEY']


def generate_response(prompt):
    response = openai.Completion.create(
        model="text-davinci-003",
        prompt=prompt,
        temperature=0.9,
        max_tokens=300,
        n=1,
        top_p=1,
        stop=None,
        frequency_penalty=0.0,
        presence_penalty=0.6,
    )

    message = response.choices[0].text.strip() # type: ignore
    message = textwrap.fill(message, width=60)
    numbered_response = ""
    lines = message.split("\n")
    for i, line in enumerate(lines):
        numbered_response += str(i+1) + ". " + line + "\n"
    return message
    # return response.choices[0].text.strip()


def chat_prompts():
    while True:
        endmsg = 'Goodbye! See you next time.'
        user_input = input("You: ")
        if user_input.lower() in ["bye", "goodbye", "end", "stop", "exit"]:
            print("ChatGPT: ",(endmsg))
            sys.exit()
        else:
            prompt = (f"User: {user_input} \nChatGPT: ")
            #prompt = f"User: {user_input}\nGPT3.5 Turbo:"
            response = generate_response(prompt)
            print("\nChatGPT:", response)
            print('')
            continue