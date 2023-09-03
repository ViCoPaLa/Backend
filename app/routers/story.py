from fastapi import APIRouter, Depends, status, HTTPException
from database import get_db
from sqlalchemy.orm import Session
from models import Scene, Chat, Mission

from internal.schema import ChatRequest
from internal.custom_exception import *
from internal.genai import *

router = APIRouter(prefix="/story", tags=["story"])

# chat, scene, mission 정보 가져오기
@router.get("/", 
            status_code=status.HTTP_200_OK,
            response_description="Success")
async def get_story_list(db: Session = Depends(get_db)):
    scene = db.query(Scene).all()
    chat = db.query(Chat).all()
    mission = db.query(Mission).all()
    return {"scene": scene, "chat": chat, "mission": mission}

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
        "scene_name": scene.scene_name,
        "background_image": scene.background_image,
        "location": scene.location,
        "description": scene.description,
        "mission": {},
        "chats": [],
        "is_user_scene": scene.is_user_scene
    }

    # Mission 정보 가져오기
    try:
        mission = db.query(Mission).filter(Mission.scene_no == scene_no).first()
        result["mission"] = {
            "mission_no": mission.mission_no,
            "mission_description": mission.mission_description,
            "mission_hint": mission.mission_hint
        }
    except:
        pass

    for chat in chats:
        if len(result["chats"]) == 0:
            result["chats"].append({
                "person": chat.person,
                "image": chat.profile,
                "message": []
            })
            result["chats"][0]["message"].append(chat.message)
        elif chat.person == result["chats"][-1]["person"]:
            result["chats"][-1]["message"].append(chat.message)
        else:
            result["chats"].append({
                "person": chat.person,
                "image": chat.profile,
                "message": []
            })
            result["chats"][-1]["message"].append(chat.message)

    return result

# 채팅 정보 저장하기
@router.post("/{scene_no}/chat",
            )
async def send_chat(scene_no: int, chat_request: ChatRequest):

    person: str = chat_request.person
    image: str = "db에서 정보 가져오기"
    message: str = chat_request.message
    
    print(person, message)

    new_person = "새로운 사람"
    prompt = new_person + " " + "이전에 말한 사람은" + person + ", 그가 한 말은 " + message
    new_message = await generate_text(prompt_text=prompt)
    
    return {"person": new_person, "image": image, "chat": new_message}