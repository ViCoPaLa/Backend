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

async def generate_text(prompt_text, n=1, max_tokens=64, temperature=0.5, top_p=1, frequency_penalty=0, presence_penalty=0, stop=["\n"]):
        
    response = openai.Completion.create(
        model="gpt-4",
        prompt=prompt_text,
        max_tokens=max_tokens,
        temperature=temperature,
        top_p=top_p,
        frequency_penalty=frequency_penalty,
        presence_penalty=presence_penalty,
        stop=stop,
        n=n
    )
    return response




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

