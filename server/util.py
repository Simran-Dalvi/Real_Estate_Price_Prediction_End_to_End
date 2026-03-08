import json
import pickle
import numpy as np
import pandas as pd

__location =None
__data_columns =None
__model = None

def load_saved_artifacts():
    # print("Loading the saved artifacts")
    global __data_columns
    global __location
    global __model

    with open(r"artifacts\columns.json") as f:
        __data_columns = json.load(f)['data_cols']
        __location = __data_columns[3:]
    
    with open(r"artifacts\banglore_house_price_model.pkl", "rb") as f:
        __model = pickle.load(f)
    
    # print("fuction... end")


def get_all_locations():
    return __location

def predict_price(location, sqft, bath, bhk):
    try:
        loc_index = __data_columns.index(location.lower())
    except:
        loc_index = -1
    x = np.zeros(len(__data_columns))
    x[0] = sqft
    x[1] = bath
    x[2] = bhk
    if loc_index >= 0:
        x[loc_index] = 1 
     
    return round(__model.predict([x])[0], 2)

if __name__ == "__main__":
    load_saved_artifacts()
    print(predict_price('1st Phase JP Nagar', 1000, 2, 2))