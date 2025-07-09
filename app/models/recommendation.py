from sqlalchemy import Column, Integer, String, Float
from app.core.db import Base

class Recommendation(Base):
    __tablename__ = "recommendations"

    id = Column(Integer, primary_key=True, index=True)
    history = Column(String)
    avg_time = Column(Float)
    cart_items = Column(String)
    purchases = Column(String)
    budget = Column(Float)
    response = Column(String)
