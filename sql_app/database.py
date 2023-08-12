from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import os
import loadenv

loadenv()
username = os.environ.get("USERNAME")
password = os.environ.get("PASSWORD")
host = os.environ.get("HOST")
database = os.environ.get("DATABASE")

# SQLALCHEMY_DATABASE_URL = "sqlite:///./database.db"
# SQLALCHEMY_DATABASE_URL = "postgresql://user:password@postgresserver/db"
SQLALCHEMY_DATABASE_URL = "mysql+pymysql://{username}:{password}@{host}:3306/{database}"


engine = create_engine(SQLALCHEMY_DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()
