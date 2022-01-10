import os
import openai

openai.api_key = os.getenv('OPENAI_API_KEY')

text_completion_input = input("Text to complete: ")

response = openai.Completion.create(
    model="curie:ft-user-xmlwcnkmjwp9z9z8berwijmz-2021-11-26-01-52-19",
    prompt="{} ->".format(text_completion_input),
    temperature=0.7,
    max_tokens=1,
    top_p=1,
    frequency_penalty=0,
    presence_penalty=0
)

print(response)