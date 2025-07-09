from fastapi import FastAPI
from app.routes import recommend
from app.core.db import Base, engine
from app.models import recommendation

Base.metadata.create_all(bind=engine)

app = FastAPI(title="E-Commerce AI with OpenAI + PostgreSQL")

app.include_router(recommend.router, prefix="/api")
