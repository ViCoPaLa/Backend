from sqlalchemy import Column, Integer, String, Text, ForeignKey,Boolean
from sqlalchemy.orm import relationship
from database import Base

class Scene(Base):
    __tablename__ = "scene"
    scene_no = Column(Integer, primary_key=True, index=True)
    scene_name = Column(String(50), nullable=False)
    background_image = Column(String(255), nullable=False)
    location = Column(String(50), nullable=False)
    description = Column(Text, nullable=False)
    is_user_scene=Column(Boolean, default=False)

    chats = relationship("Chat", back_populates="scene")
    missions = relationship("Mission", back_populates="scene")

class Chat(Base):
    __tablename__ = "chat"
    chat_id = Column(Integer, primary_key=True, index=True)
    scene_no = Column(Integer, ForeignKey("scene.scene_no"))
    person = Column(String(50), nullable=False)
    profile = Column(String(255), nullable=False)
    message = Column(Text, nullable=False)

    scene = relationship("Scene", back_populates="chats")

class Mission(Base):
    __tablename__ = 'mission'

    mission_no = Column(Integer, primary_key=True, autoincrement=True)
    scene_no = Column(Integer, ForeignKey('scene.scene_no'))
    mission_description = Column(Text)
    mission_hint = Column(Text)

    # scene_no 열과 scene 테이블 간의 관계 설정
    scene = relationship('Scene', back_populates='missions')