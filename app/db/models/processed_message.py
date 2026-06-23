# app/db/models/processed_message.py

from sqlalchemy import Column, String, TIMESTAMP
from sqlalchemy.dialects.postgresql import UUID
from app.db.database import Base
from sqlalchemy.sql import func
import uuid

class ProcessedMessage(Base):
    __tablename__ = "processed_messages"
    
    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    message_id = Column(String, nullable=False, unique=True)
    received_at = Column(TIMESTAMP, server_default=func.now(), nullable=False)
