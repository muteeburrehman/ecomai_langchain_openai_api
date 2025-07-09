from pydantic import BaseModel

class CustomerData(BaseModel):
    history: str
    avg_time: float
    cart_items: str
    purchases: str
    budget: float

class RecommendationResponse(BaseModel):
    recommendation: str
