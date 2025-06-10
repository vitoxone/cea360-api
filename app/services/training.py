# app/services/training.py
from sqlalchemy.orm import Session, joinedload
from uuid import UUID
from typing import List, Optional
from app.schemas.training import TrainingCreate, TrainingUpdate
from app.models.training import Training
from app.crud import training as crud_training

def list_trainings(db: Session, skip: int = 0, limit: int = 100) -> List[Training]:
    return crud_training.get_all_trainings(db, skip=skip, limit=limit)

def all_trainings(db: Session, skip: int = 0, limit: int = 100) -> List[Training]:
    return db.query(Training)\
        .options(joinedload(Training.assets))\
        .offset(skip)\
        .limit(limit)\
        .all()

def get_training_by_id(db: Session, training_id: UUID) -> Optional[Training]:
    return crud_training.get_training(db, training_id)

def create_new_training(db: Session, training_data: TrainingCreate) -> Training:
    return crud_training.create_training(db, training_data)

def update_existing_training(db: Session, training_id: UUID, update_data: TrainingUpdate) -> Optional[Training]:
    return crud_training.update_training(db, training_id, update_data)

def delete_training(db: Session, training_id: UUID) -> bool:
    return crud_training.soft_delete_training(db, training_id)