from fastapi import APIRouter, Depends, status, HTTPException
from database import get_db
from sqlalchemy.orm import Session
from models import Scene, Chat

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

# 특정 scene 정보 가져오기
@router.get("/{scene_no}", response_model=dict)
async def get_scene_and_chats(scene_no: int, db: Session = Depends(get_db)):

    # Scene 정보 가져오기
    scene = db.query(Scene).filter(Scene.scene_no == scene_no).first()
    if scene is None:
        db.close()
        raise HTTPException(status_code=404, detail="Scene not found")

    # Scene에 관련된 채팅 정보 가져오기
    chats = db.query(Chat).filter(Chat.scene_no == scene_no).all()

    db.close()

    # 결과를 딕셔너리로 구성
    result = {
        "scene_no": scene.scene_no,
        "background_image": scene.background_image,
        "location": scene.location,
        "hint": scene.hint,
        "message": []
    }

    for chat in chats:
        result["message"].append({
            "person": chat.person,
            "profile": chat.profile,
            "message": chat.message
        })

    return result