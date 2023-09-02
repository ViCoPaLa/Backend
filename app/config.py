from dotenv import load_dotenv
import os
from pydantic_settings import BaseSettings

load_dotenv()

# database
class DB_Settings(BaseSettings):
    db_db: str = os.getenv("DB_DB")
    db_host: str = os.getenv("DB_HOST")
    db_password: str = os.getenv("DB_PASSWORD")
    db_port: int = int(os.getenv("DB_PORT"))
    db_user: str = os.getenv("DB_USER")

# OpenAi
class OPENAI_Settings(BaseSettings):
    mytestkey: str = os.getenv("MYTESTKEY")
    organization: str = os.getenv("ORGANIZATION_NAME")
    organization_id: str = os.getenv("ORGANIZATION_ID")