import pandas as pd
import models
from database import SessionLocal, engine

db = SessionLocal()
# models.Base.metadata.create_all(bind=engine)

circuitos = pd.read_csv("datasets/circuits.csv")

carreras = pd.read_csv("datasets/races.csv")

vuelta_uno = data = pd.read_csv(
    "datasets/lap_times/lap_times_split_1.csv",
    names=["raceId", "driverId", "lap", "position", "time", "milliseconds"],
)

vuelta_dos = data = pd.read_csv(
    "datasets/lap_times/lap_times_split_2.csv",
    names=["raceId", "driverId", "lap", "position", "time", "milliseconds"],
)

vuelta_tres = data = pd.read_csv(
    "datasets/lap_times/lap_times_split_3.csv",
    names=["raceId", "driverId", "lap", "position", "time", "milliseconds"],
)

vuelta_cuatro = data = pd.read_csv(
    "datasets/lap_times/lap_times_split_4.csv",
    names=["raceId", "driverId", "lap", "position", "time", "milliseconds"],
)

vuelta_cinco = data = pd.read_csv(
    "datasets/lap_times/lap_times_split_5.csv",
    names=["raceId", "driverId", "lap", "position", "time", "milliseconds"],
)

boxes = pd.read_json("datasets/pit_stops.json")

pilotos = pd.read_json("datasets/drivers.json", lines=True)

pilotos.name = pilotos.name.astype(str)

constructores = pd.read_json("datasets/constructors.json", lines=True)

resultados = pd.read_json("datasets/results.json", lines=True)

clasificados_uno = pd.read_json("datasets/qualifying/qualifying_split_1.json")

clasificados_dos = pd.read_json("datasets/qualifying/qualifying_split_2.json")
