from sqlalchemy import Column, Integer, String, Boolean, ForeignKey
from sqlalchemy.orm import relationship
from database import Base

class Story(Base):
    __tablename__ = 'stories'
    
    id = Column(Integer, primary_key=True)
    scenes = Column(Integer)
    
    scenes_rel = relationship('Scene', back_populates='story_rel')

class Scene(Base):
    __tablename__ = 'scenes'
    
    id = Column(Integer, primary_key=True)
    story = Column(Integer, ForeignKey('stories.id'))
    chats = Column(Integer)
    
    story_rel = relationship('Story', back_populates='scenes_rel')
    chats_rel = relationship('Chat', back_populates='scene_rel')

class Chat(Base):
    __tablename__ = 'chats'
    
    id = Column(Integer, primary_key=True)
    scene = Column(Integer, ForeignKey('scenes.id'))
    name = Column(String(30))
    image = Column(String(255))
    content = Column(String(255))
    is_user_mode_start = Column(Boolean, default=False)
    
    scene_rel = relationship('Scene', back_populates='chats_rel')