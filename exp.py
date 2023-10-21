from sqlalchemy import create_engine
from sqlalchemy.exc import OperationalError


database_url = "postgresql://postgres:postgres@localhost:5432/postgres"

try:
    engine = create_engine(database_url)
    engine.connect()
    print("Соединение успешно установлено!")
except OperationalError as e:
    print(f"Ошибка соединения: {e}")
