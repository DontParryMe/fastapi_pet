from dotenv import load_dotenv
import os


load_dotenv()

db_user = os.getenv("POSTGRES_USER")
db_password = os.getenv("POSTGRES_PASSWORD")
db_name = os.getenv("POSTGRES_DB")

REAL_DATABASE_URL = f"postgresql+asyncpg://{db_user}:{db_password}@localhost:5432/{db_name}"

