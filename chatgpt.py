#OpenAI KEY: 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

import os
from openai import OpenAI

client = OpenAI(api_key="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")


text = '''
    '''

chat_completion = client.chat.completions.create(
    messages=[
        {
            "role": "user",
            "content": "Here is the Tello SDK, use these commands to control the Tello ",
        }
    ],
    model="gpt-3.5-turbo",
)



print(chat_completion.choices[0].message.content)