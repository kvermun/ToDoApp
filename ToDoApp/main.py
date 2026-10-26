from typing import Annotated
from pydantic import BaseModel, Field
from fastapi import FastAPI, Depends, HTTPException, status, Path
from sqlalchemy.orm import Session
import models
from models import Todos
from database import engine, SessionLocal
from routers import auth, todos


app = FastAPI()

models.Base.metadata.create_all(bind=engine)

app.include_router(auth.router)
app.include_router(todos.router)