#!/usr/bin/env -S rye run python

from omnistack import Omnistack

client = Omnistack()
completion = client.openai.completions.create(
    model="string",
    prompt="string",
)
print(completion)
