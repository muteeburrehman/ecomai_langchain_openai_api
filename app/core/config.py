import os
from dotenv import load_dotenv

load_dotenv()  # loads variables from .env into the environment

OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

DB_URL = (
    f"postgresql://{os.getenv('POSTGRES_USER')}:"
    f"{os.getenv('POSTGRES_PASSWORD')}@"
    f"{os.getenv('POSTGRES_HOST')}:{os.getenv('POSTGRES_PORT')}/"
    f"{os.getenv('POSTGRES_DB')}"
)
