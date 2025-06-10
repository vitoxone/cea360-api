# app/core/config.py
from pydantic import BaseSettings
from dotenv import load_dotenv
import os

# Cargar variables desde .env
load_dotenv()

class Settings(BaseSettings):
    database_url: str = os.getenv("DATABASE_URL")

settings = Settings()