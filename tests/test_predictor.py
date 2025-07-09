from app.services.predictor import predict_customer_interest
from app.core.db import SessionLocal

def test_predictor():
    db = SessionLocal()
    data = {
        "history": "headphones, speakers",
        "avg_time": 35.2,
        "cart_items": "Bluetooth headset",
        "purchases": "power bank",
        "budget": 120.0
    }
    result = predict_customer_interest(db, data)
    assert isinstance(result, str)
    assert len(result) > 10
