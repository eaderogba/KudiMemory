from app.workers.celery_app import celery_app
from app.db.database import SessionLocal
from app.db.models.processed_message import ProcessedMessage
from app.services.expense_parser import parse_expense
from app.services.whatsapp_client import send_message

CATEGORY_EMOJI = {
    "groceries": "🛒",
    "transport": "🚗",
    "food": "🍽️",
    "utilities": "💡",
    "health": "💊",
    "airtime": "📱",
    "entertainment": "🎉",
    "fuel": "⛽",
    "bills": "📄",
    "family_support": "🏠",
    "giving": "🙏",
    "miscellaneous": "📦"
}

@celery_app.task(name="process_message")
def process_message(message: dict) -> None:
    db = SessionLocal()
    try:
        message_id = message.get("id")
        message_type = message.get("type")
        from_number = message.get("from")

        if not message_id:
            return

        # Deduplication check
        existing = db.query(ProcessedMessage)\
            .filter(ProcessedMessage.message_id == message_id)\
            .first()

        if existing:
            print(f"Duplicate message {message_id}, skipping")
            return

        # Record message_id immediately — before type filtering
        # This ensures retries are caught even for non-text messages
        processed = ProcessedMessage(message_id=message_id)
        db.add(processed)
        db.commit()
        
        if message_type != "text":
            return
        
        text_body = message.get("text", {}).get("body")
        result = parse_expense(text_body)

        # Gate on confidence
        if result is None:
            reply_text = "e be like say we no fit read this one 😅 Abeg try again!"
            send_message(from_number, reply_text)
            return

        elif result["extraction_confidence"] < 0.7:
            reply_text = (
                "Hmm, we no too understand this one 🤔 "
                "Try send am like: 'fuel 5k' or 'Bolt 3500 yesterday'"
            )
            send_message(from_number, reply_text)
            return

        else:
            amount_naira = result["amount_kobo"] // 100
            category = result["category"]
            emoji = CATEGORY_EMOJI.get(category, "📦")
            reply_text = (f"Gbam! ₦{amount_naira:,} don land "
                        f"under {category.title()} {emoji} 🎯")
            send_message(from_number, reply_text)
    finally:
        db.close()
