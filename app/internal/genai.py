import os
import openai
import pandas as pd


from config import OPENAI_Settings

openai_settings = OPENAI_Settings()

MYTESTKEY = openai_settings.mytestkey
ORGANIZATION_NAME = openai_settings.organization
ORGANIZATION_ID = openai_settings.organization_id

openai.organization = ORGANIZATION_ID
openai.api_key = MYTESTKEY

# check model list
models = openai.Model.list()

data = pd.DataFrame(models["data"])
print(data.head(50))

'''
https://analyzingalpha.com/openai-api-python-tutorial
OpenAI uses DALL-E models for image processing tasks. 
The image API currently provides methods for three image-processing tasks:

1. Generating images from text.
2. Editing images based on text instructions
3. Generate image variations.
'''

# 요약된 일기를 그림으로 생성
prompt_text = "visual coding power ladies"
response = openai.Image.create(
  prompt= prompt_text,
  n=2,
  size="512x512"
)

for image in response['data']:
    print(image['url'])