import os
import openai
import pandas as pd

from config import OPENAI_Settings

openai_settings = OPENAI_Settings()

OPENAI_MYTESTKEY = openai_settings.openai_mytestkey
OPENAI_ORGANIZATION_NAME = openai_settings.openai_organization
OPENAI_ORGANIZATION_ID = openai_settings.openai_organization_id

openai.organization = OPENAI_ORGANIZATION_ID
openai.api_key = OPENAI_MYTESTKEY

# 이미지 생성
async def generate_images(prompt_text, n=1, size="512x512"):
    response = openai.Image.create(
        prompt=prompt_text,
        n=n,
        size=size
    )
    return response

async def generate_text(prompt_text, n=1, max_tokens=300, temperature=0.5, top_p=1, frequency_penalty=0, presence_penalty=0, stop=["\n"]):

    #response = "GPT에 의해 생성되는 새로운 채팅이 추후 response될 예정"
    
    message=[{"role": "user", "content": prompt_text}]

    response = openai.ChatCompletion.create(
        model="gpt-4",
        messages = message,
        temperature=0.2,
        max_tokens=max_tokens,
        frequency_penalty=0.0
    )

    return response["choices"][0]["message"]

'''
# check model list
models = openai.Model.list()
data = pd.DataFrame(models["data"])
print(data.head(50))
'''


'''
https://analyzingalpha.com/openai-api-python-tutorial
OpenAI uses DALL-E models for image processing tasks. 
The image API currently provides methods for three image-processing tasks:

1. Generating images from text.
2. Editing images based on text instructions
3. Generate image variations.
'''

