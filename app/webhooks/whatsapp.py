# app/webhooks/whatsapp.py

import os
# import requests
import hmac
import hashlib
import json
from fastapi import APIRouter, Request, HTTPException, Query
from fastapi.responses import PlainTextResponse
from app.config import config
from starlette.requests import ClientDisconnect
from app.workers.process_message import process_message

router = APIRouter()

@router.get("/webhook")
async def verify_webhook(
    hub_mode: str = Query(None, alias="hub.mode"),
    hub_challenge: str = Query(None, alias="hub.challenge"),
    hub_verify_token: str = Query(None, alias="hub.verify_token")
):
    if not hub_mode or not hub_challenge or not hub_verify_token:
        raise HTTPException(
            status_code=400, detail="Missing required query parameters")

    if hub_mode == "subscribe" and hub_verify_token == config.WHATSAPP_VERIFY_TOKEN:
        return PlainTextResponse(content=hub_challenge)

    raise HTTPException(status_code=403, detail="Verification failed")


def verify_signature(raw_body: bytes, signature_header: str) -> bool:
    if not signature_header or not signature_header.startswith("sha256="):
        return False

    received_signature = signature_header.replace("sha256=", "")

    expected_signature = hmac.new(
        key=config.WHATSAPP_APP_SECRET.encode(),
        msg=raw_body,
        digestmod=hashlib.sha256
    ).hexdigest()

    return hmac.compare_digest(received_signature, expected_signature)

def extract_messages(payload: dict) -> list[dict]:
    """
    Extract all individual messages from a webhook payload.
    Returns a list; a single payload may contain multiple messages
    """
    
    extracted_messages = []
    
    entries = payload.get("entry", [])
    
    for entry in entries:
        changes = entry.get("changes", [])
        
        for change in changes:
            value = change.get("value", {})
            messages = value.get("messages", [])
            
            for message in messages:
                extracted_messages.append(message)
                
    return extracted_messages

@router.post("/webhook")
async def receive_webhook(
    request: Request):
    try:
        raw_body = await request.body()
    except ClientDisconnect:
        return PlainTextResponse(content="OK")
    
    signature_header = request.headers.get("X-Hub-Signature-256")

    if not verify_signature(raw_body, signature_header):
        raise HTTPException(status_code=403, detail="Invalid signature")

    payload = json.loads(raw_body)
    messages = extract_messages(payload)
    
    for message in messages:
        process_message.delay(message)
            
    return PlainTextResponse(content="OK")