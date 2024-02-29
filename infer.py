from dotenv import load_dotenv
from groq import Groq

import os
import json

load_dotenv()

client = Groq(
    api_key=os.environ["GROQ_API_KEY"]
)

def infer(id, prompt, entropy):
    messages = json.loads(prompt)["messages"]
    
    completion = client.chat.completions.create(
        messages=messages,
        stop=None,
        stream=False,
        temperature=0.5,
        model="llama2-70b-4096",
        seed=int(entropy),
    )
    out = completion.choices[0].message.content
    return out