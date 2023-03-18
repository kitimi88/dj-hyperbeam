import os
from dotenv import load_dotenv
import openai
load_dotenv('./.env')

openai.api_key = os.environ['OPEN_API_KEY']


def generate_response(prompt):
    response = openai.Completion.create(
        engine = 'text-davinci-003',
        prompt = prompt,
        max_tokens = 1024,
        n = 1,
        stop = None,
        temperature = 0.9,
    )

    return response.choices[0].text.strip()


