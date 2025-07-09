from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.schemas.customer import CustomerData, RecommendationResponse
from app.services.predictor import predict_customer_interest
from app.core.db import SessionLocal

router = APIRouter()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/recommend", response_model=RecommendationResponse)
def recommend(data: CustomerData, db: Session = Depends(get_db)):
    result = predict_customer_interest(db, data.model_dump())
    return {"recommendation": result}
