from dotenv import load_dotenv
from groq import Groq

import os
import json

load_dotenv()

client = Groq(
    api_key=os.environ["GROQ_API_KEY"]
)

def infer(id, prompt, entropy):
    print(prompt)
    prompt_dict = eval(prompt)
    print(prompt_dict)

    messages = prompt_dict["messages"]
    
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

##prompt = '"\n {\n     \"messages\": [\n         {\n             \"role\": \"user\",\n             \"content\": \"Write an essay about the history, future, and current events of Bitcoin...\"\n         }\n     ]\n }\n "'
##prompt = json.loads(prompt[1:-1].replace("\n", "").replace("\t", ""))
##print(prompt["messages"])
