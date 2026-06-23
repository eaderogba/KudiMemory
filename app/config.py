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
    OPENAI_API_KEY: str = os.getenv("OPENAI_API_KEY", "")
    AWS_BUCKET_NAME: str = os.getenv("AWS_BUCKET_NAME", "")

# Single instance imported everywhere
config = Config()