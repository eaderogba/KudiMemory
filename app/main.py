# app.main.py

from fastapi import FastAPI
from app.webhooks.whatsapp import router as whatsapp_router

app = FastAPI(title="KudiTracker")

# Register the webhook router
app.include_router(whatsapp_router)

# Health check endpoint
@app.get("/health")
async def health_check():
    return {"status": "ok", "service": "kuditracker"}