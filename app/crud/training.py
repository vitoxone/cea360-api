# app/crud/training.py
from sqlalchemy.orm import Session
from uuid import UUID
from app.models.training import Training
from app.schemas.training import TrainingCreate, TrainingUpdate
from datetime import datetime
from typing import List, Optional

def get_training(db: Session, training_id: UUID) -> Optional[Training]:
    return db.query(Training).filter(Training.id == training_id, Training.deleted == False).first()

def get_all_trainings(db: Session, skip: int = 0, limit: int = 100) -> List[Training]:
    return db.query(Training).filter(Training.deleted == False).offset(skip).limit(limit).all()

def create_training(db: Session, training_data: TrainingCreate) -> Training:
    training = Training(**training_data.dict())
    db.add(training)
    db.commit()
    db.refresh(training)
    return training

def update_training(db: Session, training_id: UUID, update_data: TrainingUpdate) -> Optional[Training]:
    training = get_training(db, training_id)
    if not training:
        return None
    for key, value in update_data.dict(exclude_unset=True).items():
        setattr(training, key, value)
    training.updated_at = datetime.utcnow()
    db.commit()
    db.refresh(training)
    return training

def soft_delete_training(db: Session, training_id: UUID) -> bool:
    training = get_training(db, training_id)
    if not training:
        return False
    training.deleted = True
    training.updated_at = datetime.utcnow()
    db.commit()
    return True
