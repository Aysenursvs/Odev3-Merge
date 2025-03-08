from typing import Annotated

from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session

from models import Base
from database import engine, SessionLocal

app = FastAPI()

Base.metadata.create_all(bind=engine)