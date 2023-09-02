from fastapi import APIRouter, Depends, status
from database import get_db
from models import Book, BookInfo, BookReview
from sqlalchemy.orm import Session

router = APIRouter(prefix="/story", tags=["story"])

# 스토리 목록 보기
@router.get("/")
async def get_story_list(db: Session = Depends(get_db)):
    return get_story_list(db)
'''
response
    storties array 스토리 목록 []
        title string 스토리 제목 “세종대왕의 한글 창제 이야기”
        image string 메인 이미지 링크 “https://….png”
'''

# 특정 스토리 보기
@router.get("/{story_id}")
async def get_story(db: Session = Depends(get_db), story_id: int = 1):
    return get_story(db, story_id)
'''

'''