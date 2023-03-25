
import openai
openai.api_key = "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"

completion = openai.ChatCompletion.create(
  model="gpt-3.5-turbo",
  messages=[
    {"role": "user", "content": "You are a customer in a coffee shop. Provide a 10 word sentence response as if the barrista made your drink right"}
  ]
)

print(completion.choices[0].message.content)