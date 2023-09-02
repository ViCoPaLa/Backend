from sqlalchemy import Column, Text, Integer, Boolean, String, TIMESTAMP, Date, DateTime, DECIMAL, SmallInteger, text, ForeignKey
from sqlalchemy.dialects.mysql import INTEGER
from sqlalchemy.orm import relationship
from database import Base

UnsignedInt = INTEGER()
UnsignedInt = UnsignedInt.with_variant(INTEGER(unsigned=True), 'mysql')

class Stories(Base):
    pass

class Scenes(Base):
    pass

class Charts(Base):
    pass