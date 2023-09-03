from pydantic import BaseModel, validator
from typing import List
from internal.custom_exception import InvalidDateFormatError
import datetime

class ChatRequest(BaseModel):
    person: str
    message: str