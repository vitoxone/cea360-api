# app/routes/training.py
from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from uuid import UUID
from typing import List

from app.schemas.training import TrainingCreate, TrainingUpdate, TrainingOut
from app.services import training as training_service
from app.core.database import SessionLocal

router = APIRouter(prefix="/trainings", tags=["Trainings"])

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.get("/", response_model=List[TrainingOut])
def list_trainings(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    return training_service.all_trainings(db, skip, limit)

@router.get("/{training_id}", response_model=TrainingOut)
def get_training(training_id: UUID, db: Session = Depends(get_db)):
    training = training_service.get_training_by_id(db, training_id)
    if not training:
        raise HTTPException(status_code=404, detail="Training not found")
    return training

@router.post("/", response_model=TrainingOut, status_code=status.HTTP_201_CREATED)
def create_training(training_data: TrainingCreate, db: Session = Depends(get_db)):
    return training_service.create_new_training(db, training_data)

@router.put("/{training_id}", response_model=TrainingOut)
def update_training(training_id: UUID, update_data: TrainingUpdate, db: Session = Depends(get_db)):
    training = training_service.update_existing_training(db, training_id, update_data)
    if not training:
        raise HTTPException(status_code=404, detail="Training not found")
    return training

@router.delete("/{training_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_training(training_id: UUID, db: Session = Depends(get_db)):
    success = training_service.delete_training(db, training_id)
    if not success:
        raise HTTPException(status_code=404, detail="Training not found")
