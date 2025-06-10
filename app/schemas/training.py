# app/schemas/training.py

from pydantic import BaseModel
from typing import List, Optional
from uuid import UUID
from datetime import datetime
from app.schemas.training_asset import TrainingAssetOut  # Asegúrate que este está definido

class TrainingBase(BaseModel):
    title: str
    description: Optional[str] = None
    area: Optional[str] = None
    is_free: bool = False
    price: Optional[int] = None

class TrainingCreate(TrainingBase):
    pass

class TrainingUpdate(BaseModel):
    title: Optional[str] = None
    description: Optional[str] = None
    area: Optional[str] = None
    is_free: Optional[bool] = None
    price: Optional[int] = None
    status: Optional[str] = None
    deleted: Optional[bool] = None

class TrainingOut(TrainingBase):
    id: UUID
    status: str
    deleted: bool
    created_at: datetime
    updated_at: datetime
    assets: List[TrainingAssetOut] = []

    class Config:
        from_attributes = True  # <- usa esto en Pydantic v2