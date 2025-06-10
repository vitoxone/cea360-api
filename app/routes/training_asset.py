from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.orm import Session
from uuid import UUID
from typing import List

from app.schemas.training import TrainingAssetCreate, TrainingAssetSchema
from app.services import training_asset_service
from app.core.database import SessionLocal

router = APIRouter(prefix="/training-assets", tags=["Training Assets"])

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/", response_model=TrainingAssetSchema)
def create_asset(asset: TrainingAssetCreate, db: Session = Depends(get_db)):
    return training_asset_service.create_asset(db, asset)

@router.get("/{asset_id}", response_model=TrainingAssetSchema)
def get_asset(asset_id: UUID, db: Session = Depends(get_db)):
    db_asset = training_asset_service.get_asset(db, asset_id)
    if db_asset is None:
        raise HTTPException(status_code=404, detail="Asset not found")
    return db_asset

@router.get("/", response_model=List[TrainingAssetSchema])
def list_assets(db: Session = Depends(get_db)):
    return training_asset_service.list_assets(db)

@router.delete("/{asset_id}")
def delete_asset(asset_id: UUID, db: Session = Depends(get_db)):
    success = training_asset_service.delete_asset(db, asset_id)
    if not success:
        raise HTTPException(status_code=404, detail="Asset not found")
    return {"detail": "Asset deleted successfully"}