from dotenv import load_dotenv
from groq import Groq

import os
import json

load_dotenv()

client = Groq(
    api_key=os.environ["GROQ_API_KEY"]
)

def infer(model_id, prompt, entropy):
    prompt_dict = eval(prompt)
    messages = prompt_dict["messages"]
    
    if model_id == 12:
        completion = client.chat.completions.create(
            messages=messages,
            stop=None,
            stream=False,
            temperature=0.5,
            model="llama2-70b-4096",
            seed=int(entropy),
        )
    elif model_id == 14:
        completion = client.chat.completions.create(
            messages=messages,
            stop=None,
            stream=False,
            temperature=0.5,
            model="gemma-7b-it",
            seed=int(entropy),
        )
    elif model_id == 16:
        completion = client.chat.completions.create(
            messages=messages,
            stop=None,
            stream=False,
            temperature=0.5,
            model="mixtral-8x7b-32768",
            seed=int(entropy),
        )
    
    out = completion.choices[0].message.content
    return out
