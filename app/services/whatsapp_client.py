# app/services/whatsapp_client.py

import httpx
from app.config import config

def send_message(to: str, message: str) -> bool:
    url = (
        f"https://graph.facebook.com/v19.0/"
        f"{config.WHATSAPP_PHONE_NUMBER_ID}/messages"
    )
    
    headers = {
        "Authorization": f"Bearer {config.WHATSAPP_TOKEN}",
        "Content-Type": "application/json" 
    }
    
    payload = {
        "messaging_product": "whatsapp",
        "to": to,
        "type": "text",
        "text": {"body": message}
    }
    
    try:
        response = httpx.post(url, json=payload, headers=headers, timeout=10)
        return response.status_code == 200
    
    except Exception as e:
        print(f"Failed to send whatsapp message: {e}")
        return False