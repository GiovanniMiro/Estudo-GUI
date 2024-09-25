#import openai
from groq import Groq

client = Groq(api_key="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")

completion = client.chat.completions.create(
  model="llama3-8b-8192",
  messages=[
    {"role": "user", "content": "Que tipo de gato é um tuxedo cat?"}
  ],
    max_tokens=1000, #Num max de palavras
    temperature=0.7,   #Criatividade
    n=1              #Num de respostas
)

print(completion.choices[0].message.content)