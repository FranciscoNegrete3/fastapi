import pandas as pd
import models
from database import SessionLocal, engine

db = SessionLocal()
#models.Base.metadata.create_all(bind=engine)

circuits=pd.read_csv("datasets/circuits.csv")
races=pd.read_csv("datasets/races.csv")
lapTime_1=data= pd.read_csv('datasets/lap_times/lap_times_split_1.csv', names=["raceId","driverId","lap","position","time","milliseconds"])
lapTime_2=data= pd.read_csv('datasets/lap_times/lap_times_split_2.csv', names=["raceId","driverId","lap","position","time","milliseconds"])
lapTime_3=data= pd.read_csv('datasets/lap_times/lap_times_split_3.csv', names=["raceId","driverId","lap","position","time","milliseconds"])
lapTime_4=data= pd.read_csv('datasets/lap_times/lap_times_split_4.csv', names=["raceId","driverId","lap","position","time","milliseconds"])
lapTime_5=data= pd.read_csv('datasets/lap_times/lap_times_split_5.csv', names=["raceId","driverId","lap","position","time","milliseconds"])
pitStops =  pd.read_json('datasets/pit_stops.json')
drivers = pd.read_json('datasets/drivers.json', lines = True )
drivers.name=drivers.name.astype(str)
constructors = pd.read_json('datasets/constructors.json', lines = True)
results = pd.read_json('datasets/results.json', lines = True)
qualifying_1 = pd.read_json('datasets/qualifying/qualifying_split_1.json')
qualifying_2 = pd.read_json('datasets/qualifying/qualifying_split_2.json')



# drivers.to_sql(name="drivers", con=engine, if_exists='append', index=False)
# constructors.to_sql(name="constructors", con=engine, if_exists='append', index=False)
# circuits.to_sql(name="circuits", con=engine, if_exists='append', index=False)

# races.to_sql(name='races', con=engine, if_exists='append', index=False)
# results.to_sql(name="results", con=engine, if_exists='append', index=False)
# pitStops.to_sql(name="pitstops", con=engine, if_exists='append', index=False)
# lapTime_1.to_sql(name='laptimes', con=engine, if_exists='append', index=False)
# lapTime_2.to_sql(name='laptimes', con=engine, if_exists='append', index=False)
# lapTime_3.to_sql(name='laptimes', con=engine, if_exists='append', index=False)
# lapTime_4.to_sql(name='laptimes', con=engine, if_exists='append', index=False)
# lapTime_5.to_sql(name='laptimes', con=engine, if_exists='append', index=False)
# qualifying_1.to_sql(name="qualifying", con=engine, if_exists='append', index=False)
# qualifying_2.to_sql(name="qualifying", con=engine, if_exists='append', index=False)


db.commit()

db.close()

#print(type(qualifying_1))