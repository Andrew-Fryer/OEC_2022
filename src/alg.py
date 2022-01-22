import numpy as np
import math
import pandas as pd

# csv file, a, b
def alg(df, risk_weight, distance_weight):
    # decide on optimal order for each specific set of waste
    # paths order [[local_sorting_idx, regional_sorting_idx, regional_recycling_idx],...]
    paths = []

    waste_facility = df[df.iloc[:,3].str.contains('waste')]
    local_sorting = df[df.iloc[:,3].str.contains('local_sorting_facility')]
    regional_sorting = df[df.iloc[:,3].str.contains('regional_sorting_facility')]
    regional_recycling = df[df.iloc[:,3].str.contains('regional_recycling_facility')]

    for idx, row in waste_facility.iterrows():
        temp = [idx]
        # Waste to local sorting
        local_sorting_idx = optimal_facility(row, local_sorting, risk_weight, distance_weight)
        temp.append(local_sorting_idx)

        # local sorting to regional sorting
        regional_sorting_idx = optimal_facility(local_sorting.iloc[local_sorting_idx], regional_sorting, risk_weight, distance_weight)
        temp.append(regional_sorting_idx)

        # local sorting to regional sorting
        regional_recycling_idx = optimal_facility(regional_sorting.iloc[regional_sorting_idx], regional_recycling, risk_weight, distance_weight)
        temp.append(regional_recycling_idx)

        paths.append(temp)

    return paths

def risk(facility_risk, distance_travelled, amount_processing):
    return facility_risk*distance_travelled*amount_processing

# moving waste to local sorting facility 
def optimal_facility(facility1, facility2, a, b):
    scores = []
    for idx, row in facility2.iterrows():
        distance = get_delta_distance([facility1["latitude"], facility1["longitude"]],[row["latitude"], row["longitude"]])
        risk_value = risk(row["risk"], distance, facility1["amount"])
        scores.append(score(a, b, risk_value, distance))
    # greedily chooose minimum score for facility to go to
    min_score = min(scores)
    min_score_idx = scores.index(min_score)
    # return row index for specfied facility2 dataframe
    return min_score_idx


def score(a, b, risk, distance):
    return a*risk + b*distance

def get_delta_distance(latLon1, latLon2):
    
    R = 6371
    x1_lat, y1_lon = latLon1
    x2_lat, y2_lon = latLon2
    #print(x1_lat, ",", y1_lon)
    latavg = (int(x1_lat) + int(x2_lat))/2

    x1 = R * int(y1_lon) * math.cos(latavg)
    y1 = R * int(x1_lat)

    x2 = R * int(y2_lon) * math.cos(latavg)
    y2 = R * int(x2_lat)

    return math.hypot(abs(x1-x2), abs(y1-y2))/1000


df = pd.read_csv("./data/small/test_10_equal.csv",header=None,names = ['id','latitude','longitude','type','amount','risk'])
print(alg(df, 1, 1))