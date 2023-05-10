# Import the ask_chatgpt function
import openai
from openai import ask_chatgpt

# Set your OpenAI API key
openai_api_key = "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"

# Set the prompt
prompt = "proverb with word 'success'"

# Generate text using the OpenAI API and the ask_chatgpt function
response = ask_chatgpt(prompt, openai_api_key)

# Print the generated text
print(response)
