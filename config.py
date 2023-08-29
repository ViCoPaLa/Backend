from dotenv import load_dotenv
import os
from pydantic_settings import BaseSettings

load_dotenv()

class OPENAI_Settings(BaseSettings):
    mytestkey: str = os.getenv("MYTESTKEY")
    organization: str = os.getenv("ORGANIZATION_NAME")
    organization_id: str = os.getenv("ORGANIZATION_ID")