from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import os
from dotenv import load_dotenv

load_dotenv()
# username = os.getenv("DB_USERNAME")
# password = os.getenv("DB_PASSWORD")
# host = os.getenv("DB_HOST")
# database = os.getenv("DB_DATABASE")

SQLALCHEMY_DATABASE_URL = "sqlite:///database.db"
# SQLALCHEMY_DATABASE_URL = "postgresql://user:password@postgresserver/db"
# SQLALCHEMY_DATABASE_URL = (
#     f"mysql+pymysql://{username}:{password}@{host}:3306/{database}"
# )

engine = create_engine(
    SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False}
)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()
