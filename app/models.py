from sqlalchemy import Column, Integer, String, Text, ForeignKey
from sqlalchemy.orm import relationship
from database import Base

class Scene(Base):
    __tablename__ = "scene"
    scene_no = Column(Integer, primary_key=True, index=True)
    background_image = Column(String(255), nullable=False)
    location = Column(String(50), nullable=False)
    hint = Column(Text, nullable=False)

    chats = relationship("Chat", back_populates="scene")

class Chat(Base):
    __tablename__ = "chat"
    chat_id = Column(Integer, primary_key=True, index=True)
    scene_no = Column(Integer, ForeignKey("scene.scene_no"))
    person = Column(String(50), nullable=False)
    profile = Column(String(255), nullable=False)
    message = Column(Text, nullable=False)

    scene = relationship("Scene", back_populates="chats")