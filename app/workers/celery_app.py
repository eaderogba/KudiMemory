from celery import Celery
from app.config import config

celery_app = Celery(
    "kuditracker",
    broker=config.REDIS_URL,
    backend=config.REDIS_URL,
    include=["app.workers.process_message"]
)

celery_app.conf.update(
    task_serializer="json",
    accept_content=["json"],
    result_serializer="json",
    timezone="Africa/Lagos",
    task_track_started=True,
    task_acks_late=True,           # ack after task finishes — safer if worker crashes
    worker_prefetch_multiplier=1,  # fair for message processing
)
