from pydantic import BaseModel, HttpUrl, Field
from typing import List, Optional
from uuid import UUID
from datetime import datetime

class TrainingAssetBase(BaseModel):
    type: str
    title: Optional[str] = None
    url: HttpUrl

class TrainingAssetCreate(TrainingAssetBase):
    training_id: UUID

class TrainingAsset(TrainingAssetBase):
    id: UUID
    training_id: UUID
    status: Optional[str]
    deleted: bool
    created_at: datetime
    updated_at: datetime

    class Config:
        from_attributes = True

class TrainingAssetOut(BaseModel):
    id: UUID
    title: str
    type: str
    url: str
    created_at: datetime
    updated_at: datetime

    class Config:
        from_attributes = True