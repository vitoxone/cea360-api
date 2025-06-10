# app/models/training.py
from sqlalchemy import Column, String, Text, Integer, Boolean, ForeignKey, Enum, DateTime
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import relationship
from app.models.training import Training
from datetime import datetime
import uuid
from app.core.database import Base


class TrainingAsset(Base):
    __tablename__ = "training_assets"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4, index=True)
    training_id = Column(UUID(as_uuid=True), ForeignKey("trainings.id"), nullable=False)
    type = Column(String)  # video, pdf, audio, image
    title = Column(String)
    url = Column(Text, nullable=False)
    status = Column(String, default="active")
    deleted = Column(Boolean, default=False)
    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

    training = relationship(Training, back_populates="assets")