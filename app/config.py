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
    openai_mytestkey: str = os.getenv("OPENAI_MYTESTKEY")
    openai_organization: str = os.getenv("OPENAI_ORGANIZATION_NAME")
    openai_organization_id: str = os.getenv("OPENAI_ORGANIZATION_ID")