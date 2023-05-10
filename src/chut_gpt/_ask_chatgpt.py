import openai
import os

def ask_chatgpt(prompt):
    # Set up OpenAI API credentials
    openai.api_key = "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"

    # Set up prompt and parameters for the API request
    prompt = f"{prompt}\n\nAnswer:"
    parameters = {
        "prompt": prompt,
        "temperature": 0.5,
        "max_tokens": 1000,
        "nogpt-3": True
    }

    # Send request to the OpenAI API and get response
    response = openai.Completion.create(parameters)
    answer = response.choices[0].text.strip()

    return answer

print(ask_chatgpt('what is smalltalk ?'))