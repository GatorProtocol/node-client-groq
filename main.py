from gator import Model
from infer import infer

import threading

import os
import sys

from dotenv import load_dotenv
load_dotenv()

def fail():
    print("TASK FAILED")

llama = Model(
    callback=infer,
    id=12,
    provider=os.environ["PROVIDER"],
    boost=1,
    env=dict(os.environ),
    errorcallback=fail,
    checkfreq=1,
)

gemma = Model(
    callback=infer,
    id=14,
    provider=os.environ["provider"],
    boost=1,
    env=dict(os.environ),
    errorcallback=fail,
    checkfreq=1
)

mistral = Model(
    callback=infer,
    id=16,
    provider=os.environ["PROVIDER"],
    boost=1,
    env=dict(os.environ),
    errorcallback=fail,
    checkfreq=1,
)

llama_thread = threading.Thread(target=llama.start)
mistral_thread = threading.Thread(target=mistral.start)
gemma_thread = threading.Thread(target=gemma.start)

llama_thread.start()
mistral_thread.start()
gemma_thread.start()