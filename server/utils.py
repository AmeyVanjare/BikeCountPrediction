import json
import pickle
import numpy as np
import pandas as pd

__data_columns = None
__model = None

def get_estimated_count(season,workingday,temp,atemp,humidity,windspeed):
    global __model
    x =np.zeros(len(__data_columns))
    x[0]= season
    x[2]= workingday
    x[4]= temp
    x[5]= atemp
    x[6]= humidity
    x[7]= windspeed
    #print(x)
    return round((__model.predict([x])[0]),2)

def load_saved_artifacts():
    print("Loading saved artifacts.....Start")
    global __data_columns
    global __model
    with open("server/artifacts/columns.json",'r') as f:
        __data_columns = json.load(f)['data_columns']

    with open("server/artifacts/Bike_Casual_Count_model.pickle",'rb') as f:
        __model = pickle.load(f)

    print("Loading saved artifacts.....Done")

if __name__ == "__main__":
    load_saved_artifacts()
    print('abc')
    print("Estimated count of casual bikers ",get_estimated_count(2,1,16.40,20.45,76,32))
