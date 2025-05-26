from sqlmodel import SQLModel, create_engine, Session
from seredra.models.sql_models import WeatherEntry

DATABASE_URL = "sqlite:///seredra.db"
engine = create_engine(DATABASE_URL, echo=True)

def init_db() -> None:
	SQLModel.metadata.create_all(engine)

def get_session() -> Session:
	return Session(engine)