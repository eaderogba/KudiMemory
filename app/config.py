import os
from dotenv import load_dotenv

load_dotenv()

class Config:
    WHATSAPP_TOKEN: str = os.getenv("WHATSAPP_TOKEN", "")
    WHATSAPP_VERIFY_TOKEN: str= os.getenv("WHATSAPP_VERIFY_TOKEN", "")
    WHATSAPP_PHONE_NUMBER_ID: str = os.getenv("WHATSAPP_PHONE_NUMBER_ID")
    WHATSAPP_APP_SECRET: str = os.getenv("WHATSAPP_APP_SECRET")
    
    DATABASE_URL: str = os.getenv("DATABASE_URL", "")
    REDIS_URL: str = os.getenv("REDIS_URL", "")

    OPENAI_API_KEY = os.getenv("OPENAI_API_KEY", "")
    OPENAI_MODEL = os.getenv("OPENAI_MODEL", "gpt-4o-mini")
    
    # app/config.py


    OLLAMA_BASE_URL = "http://localhost:11434/v1"
    OLLAMA_MODEL = "llama3:latest"

    AWS_BUCKET_NAME: str = os.getenv("AWS_BUCKET_NAME", "")

# Single instance imported everywhere
config = Config()