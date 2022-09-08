from sqlalchemy import Column, Integer, String, Float, DateTime, ForeignKey
from database import Base


class races(Base):
    __tablename__ = "races"
    raceId = Column(Integer, index=True, primary_key=True)
    year = Column(Integer)
    round = Column(Integer)
    circuitId = Column(Integer, ForeignKey("circuits.circuitId"))
    name = Column(String(255))
    date = Column(String(255))
    time = Column(String(255))
    url = Column(String(255))

    class Config:
        orm_mode = True


class circuits(Base):
    __tablename__ = "circuits"
    circuitId = Column(Integer, index=True, primary_key=True)
    circuitRef = Column(String(255))
    name = Column(String(255))
    location = Column(String(255))
    country = Column(String(255))
    lat = Column(Float)
    lng = Column(Float)
    alt = Column(Integer)
    url = Column(String(255))

    class Config:
        orm_mode = True


class lapTimes(Base):
    __tablename__ = "laptimes"
    lapTimesId = Column(Integer, primary_key=True, autoincrement=True)
    raceId = Column(Integer, ForeignKey("races.raceId"))
    driverId = Column(Integer, ForeignKey("drivers.driverId"))
    lap = Column(Integer)
    position = Column(Integer)
    time = Column(String(255))
    milliseconds = Column(Integer)

    class Config:
        orm_mode = True


class pitStops(Base):
    __tablename__ = "pitstops"
    pitStopsId = Column(Integer, index=True, primary_key=True, autoincrement=True)
    raceId = Column(Integer, ForeignKey("races.raceId"))
    driverId = Column(Integer, ForeignKey("drivers.driverId"))
    stop = Column(Integer)
    lap = Column(Integer)
    time = Column(String(255))
    duration = Column(String(255))
    milliseconds = Column(Integer)

    class Config:
        orm_mode = True


class drivers(Base):
    __tablename__ = "drivers"
    driverId = Column(Integer, index=True, primary_key=True)
    driverRef = Column(String(255))
    number = Column(String(255))
    code = Column(String(255))
    name = Column(String(255))
    dob = Column(String(255))
    nationality = Column(String(255))
    url = Column(String(255))

    class Config:
        orm_mode = True


class constructors(Base):
    __tablename__ = "constructors"
    constructorId = Column(Integer, index=True, primary_key=True)
    constructorRef = Column(String(255))
    name = Column(String(255))
    nationality = Column(String(255))
    url = Column(String(255))

    class Config:
        orm_mode = True


class results(Base):
    __tablename__ = "results"
    resultId = Column(Integer, index=True, primary_key=True)
    raceId = Column(Integer, ForeignKey("races.raceId"))
    driverId = Column(Integer, ForeignKey("drivers.driverId"))
    constructorId = Column(Integer, ForeignKey("constructors.constructorId"))
    number = Column(String(255))
    grid = Column(Integer)
    position = Column(String(255))
    positionText = Column(String(255))
    positionOrder = Column(Integer)
    points = Column(Float)
    laps = Column(Integer)
    time = Column(String(255))
    milliseconds = Column(String(255))
    fastestLap = Column(String(255))
    rank = Column(String(255))
    fastestLapTime = Column(String(255))
    fastestLapSpeed = Column(String(255))
    statusId = Column(Integer)

    class Config:
        orm_mode = True


class qualifying(Base):
    __tablename__ = "qualifying"
    qualifyId = Column(Integer, index=True, primary_key=True)
    raceId = Column(Integer, ForeignKey("races.raceId"))
    driverId = Column(Integer, ForeignKey("drivers.driverId"))
    constructorId = Column(Integer, ForeignKey("constructors.constructorId"))
    number = Column(Integer)
    position = Column(Integer)
    q1 = Column(String(255))
    q2 = Column(String(255))
    q3 = Column(String(255))

    class Config:
        orm_mode = True
