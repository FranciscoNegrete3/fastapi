from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
#import PyMySQL

# user = input('Ingrese nombre de usuario:' )
# password = input('Ingrese contraseña:' )
# database = input('Ingrese nombre de la base de datos:' )

#engine = create_engine(f"mysql+pymysql://{user}:{password}@localhost:3306/{database}")
engine = create_engine("mysql+pymysql://root:Bufalo4030@localhost:3306/henrydb")

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()

conn = engine.connect()
