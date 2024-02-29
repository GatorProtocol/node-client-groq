from gator import Model
from infer import infer

import os
import sys

from dotenv import load_dotenv
load_dotenv()

model = Model(
    callback=infer,
    id=12,
    provider=os.environ["PROVIDER"],
    boost=1,
    env=dict(os.environ),
    errorcallback=sys.exit,
    checkfreq=3
)
model.start()