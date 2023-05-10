import openai


def ask_gpt(prompt_text):
    openai.api_key = "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"
    # Set up the request parameters
    model_engine = "text-davinci-002"
    prompt = prompt_text
    completions = openai.Completion.create(
        engine=model_engine,
        prompt=prompt,
        max_tokens=1024,
        n=1,
        stop=None,
        temperature=0.5,
    )
    # Get the response from the API
    response = completions.choices[0].text
    return response


def get_words_proverbs(word):
    prompt_text = f"""
please, give me all single-root words and all forms for the word {word}  with theirs translate on russian.
and most popular phrases, better proverbs or aphorisms, with some of these words with translate on russian.
"""
    print(ask_gpt(prompt_text))


word = 'neck'
# get_words_proverbs(word)
