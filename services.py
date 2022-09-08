import database
import sqlalchemy.orm as _orm

def create_database():
    return database.Base.metadata.create_all(bind=database.engine)