from asyncio import streams
from tokenize import Floatnumber
from fastapi import FastAPI
from load_2 import *
from pydantic import BaseModel
import pandas as pd
import json

app = FastAPI()


def parse_csv(df):
    res = df.to_json(orient="records")
    parsed = json.loads(res)
    return parsed


class Circuito(BaseModel):
    circuitId: int
    circuitRef: str
    name: str
    location: str
    country: str
    lat: float
    lng: float
    alt: int
    url: str


nuevo_circuito = []


@app.get("/circuitos")
async def get_circuitos():
    result = parse_csv(circuitos)
    return result[0:5]


@app.get("/circuito/{country}")
async def get_circuito(country: str):
    result = parse_csv(circuitos)

    found_circuits = []

    for x in result:
        if x["country"] == country:

            found_circuits.append(x)

            return found_circuits


@app.post("/post_circuitos")
async def post_circuitos(circuito: Circuito):
    nuevo_circuito.append(circuito.dict())
    return nuevo_circuito


@app.get("/carreras")
async def get_carreras():
    return parse_csv(carreras)


@app.post("/post_carreras")
async def post_carreras(
    raceId: int,
    year: int,
    round: int,
    circuitId: int,
    name: str,
    date: str,
    time: str,
    url: str,
):
    return "Nueva carrera almacenada!"


@app.get("/vuelta_uno")
async def get_vuelta_uno():
    return parse_csv(vuelta_uno)


@app.post("/post_vuelta_uno")
async def post_vuelta_uno(
    lapTimesId: int,
    raceId: int,
    driverId: int,
    lap: int,
    position: int,
    time: str,
    milliseconds: int,
):
    return "Primera vuelta almacenada!"


@app.get("/vuelta_dos")
async def get_vuelta_dos():
    return parse_csv(vuelta_dos)


@app.post("/post_vuelta_dos")
async def post_vuelta_dos(
    lapTimesId: int,
    raceId: int,
    driverId: int,
    lap: int,
    position: int,
    time: str,
    milliseconds: int,
):
    return "Segunda vuelta almacenada!"


@app.get("/vuelta_tres")
async def get_vuelta_tres():
    return parse_csv(vuelta_tres)


@app.post("/post_vuelta_tres")
async def post_vuelta_tres(
    lapTimesId: int,
    raceId: int,
    driverId: int,
    lap: int,
    position: int,
    time: str,
    milliseconds: int,
):
    return "Tercera vuelta almacenada!"


@app.get("/vuelta_cuatro")
async def get_vuelta_cuatro():
    return parse_csv(vuelta_cuatro)


@app.post("/post_vuelta_cuatro")
async def post_vuelta_cuatro(
    lapTimesId: int,
    raceId: int,
    driverId: int,
    lap: int,
    position: int,
    time: str,
    milliseconds: int,
):
    return "Cuarta vuelta almacenada!"


@app.get("/vuelta_cinco")
async def get_vuelta_cinco():

    result = parse_csv(vuelta_cinco)
    return result[0:5]


@app.post("/post_vuelta_cinco")
async def post_vuelta_cinco(
    lapTimesId: int,
    raceId: int,
    driverId: int,
    lap: int,
    position: int,
    time: str,
    milliseconds: int,
):
    return "Quinta vuelta almacenada!"


@app.get("/boxes")
async def get_boxes():
    return parse_csv(boxes)


@app.post("/post_boxes")
async def post_boxes(
    pitStopsId: int,
    raceId: int,
    driverId: int,
    stop: int,
    lap: int,
    time: str,
    duration: str,
    milliseconds: int,
):
    return "Nueva parada en Boxes almacenada!"


@app.get("/pilotos")
async def get_pilotos():
    return parse_csv(pilotos)


@app.post("/post_pilotos")
async def post_pilotos(
    driverId: int,
    driverRef: str,
    number: str,
    code: str,
    name: str,
    dob: str,
    nationality: str,
    url: str,
):
    return "Nuevo piloto almacenado!"


@app.get("/constructores ")
async def get_constructores():
    return parse_csv(constructores)


@app.post("/post_constructores")
async def post_constructores(
    constructorId: int, constructorRef: str, name: str, nationality: str, url: str
):
    return "Nuevo constructor almacenado!"


@app.get("/resultados")
async def get_resultados():
    return parse_csv(resultados)


@app.post("/post_resultados")
async def post_resultados(
    resultId: int,
    raceId: int,
    driverId: int,
    constructor: int,
    number: str,
    grid: int,
    position: str,
    positionText: str,
    positionOrder: int,
    points: float,
    laps: int,
    time: str,
    milliseconds: str,
    fastestlap: str,
    rank: str,
    fastestLapSpeed: str,
    statusId: int,
):
    return "Nuevo resultado almacenado!"


@app.get("/clasificados_uno")
async def load_questions():
    return parse_csv(clasificados_uno)


@app.post("/post_clasificados_uno")
async def post_clasificados_uno(
    qualifyId: int,
    raceId: int,
    driverId: int,
    constructorId: int,
    number: int,
    position: int,
    q1: str,
    q2: str,
    q3: str,
):
    return "Nuevos clasificados almacenados!"


@app.get("/clasificados_dos")
async def get_clasificados_dos():
    return parse_csv(clasificados_dos)


@app.post("/post_clasificados_dos")
async def post_clasificados_dos(
    qualifyId: int,
    raceId: int,
    driverId: int,
    constructorId: int,
    number: int,
    position: int,
    q1: str,
    q2: str,
    q3: str,
):
    return "Nuevos clasificados segunda vuelta almacenados!"
