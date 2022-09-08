#import imp
import database
from database import engine
from database import conn 
import load
import models
from models import races
from fastapi import FastAPI, Depends
from fastapi.responses import JSONResponse
import pydantic
from pydantic import BaseModel
from typing import List, Optional
from uuid import uuid4
import pandas as pd

import services

#models.Base.metadata.create_all(bind=engine)

services.create_database()

app = FastAPI()

@app.get("/hola")
async def mensaje():
    return "Hola Mundo"


@app.get("/races")
async def get_races():
    
    test = type(races)

    return test

