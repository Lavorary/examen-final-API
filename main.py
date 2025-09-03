import base64
import numbers
from typing import List

from fastapi import FastAPI
from pydantic import BaseModel
from starlette.requests import Request
from starlette.responses import Response, JSONResponse

app = FastAPI()

@app.get("/ping")
async def ping():
    return Response(content="pong", status_code=200, media_type="text/plain")


class Characteristic(BaseModel):
    max_speed: numbers.Number
    min_speed: numbers.Number


@app.post("/cars")
async def cars():
    identifier : str
    brand : str
    model : str
    characteristics : Characteristic

