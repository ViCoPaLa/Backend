from fastapi import APIRouter, Depends, status
from database import get_db
from sqlalchemy.orm import Session
from internal.genai import *

router = APIRouter(prefix="/generate", tags=["generate"])

# 이미지 생성
@router.get("/image",
            status_code=status.HTTP_200_OK,
            response_description="Generate Image")
async def gen_image(prompt: str):
    return generate_images(prompt)

# 텍스트 생성
@router.get("/text",
            status_code=status.HTTP_200_OK,
            response_description="Generate Text")
async def gen_text(prompt: str):
    return generate_text(prompt)