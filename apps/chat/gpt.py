import os
from dotenv import load_dotenv
import openai
load_dotenv('./.env')
import textwrap
openai.api_key = os.environ['OPEN_API_KEY']


def generate_response(prompt):
    response = openai.Completion.create(
        model="text-davinci-003",
        prompt=prompt,
        temperature=0.9,
        max_tokens=2048,
        n=1,
        top_p=1,
        stop=None,
        frequency_penalty=0.0,
        presence_penalty=0.6,
    )

    message = response.choices[0].text.strip()
    message = textwrap.fill(message, width=60)
    numbered_response = ""
    lines = message.split("\n")
    for i, line in enumerate(lines):
        numbered_response += str(i+1) + ". " + line + "\n"
    return message
    # return response.choices[0].text.strip()


