import base64
import numbers
from typing import List

from fastapi import FastAPI
from pydantic import BaseModel
from starlette.requests import Request
from starlette.responses import Response, JSONResponse

app = FastAPI()

@app.get("/ping")
def ping():
    return Response(content="pong", status_code=200, media_type="text/plain")




class Characteristic(BaseModel):
    max_speed: int
    min_fuel_capacity: int


class Cars:
    identifier : str
    brand : str
    model : str
    characteristics : Characteristic


cars_stored = List[Cars] = []


def car_serialized():
    car_serialized = []
    for c in cars_stored:
        car_serialized.append(c.model_dump())
    return car_serialized



@app.post("/cars")
def cars(car_paylod: List[Cars]):
    cars_stored.append(car_paylod)
    serilized_car = car_serialized()
    return JSONResponse(content=serilized_car, status_code=201, media_type="application/json")











