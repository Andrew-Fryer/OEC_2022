import numpy as np
import math
import pandas as pd

# csv file, a, b
def alg(df, risk_weight, distance_weight):
    # decide on optimal order for each specific set of waste
    paths = []
    waste_facility = []
    local_sorting = []
    regional_sorting = []
    regional_recycling = []

    for i in range(len(waste_facility)):
        temp = []
        temp.append(optimal_facility())    

    return 0

def risk(facility_risk, distance_travelled, amount_processing):
    return facility_risk*distance_travelled*amount_processing

# moving waste to local sorting facility -> sortinf facility as dictionary with row elements
def optimal_facility(w_long, w_lat, w_amount, sorting, a, b):
    scores = []
    for s in sorting:
        distance = get_delta_distance([w_long, w_lat],[s["latitude"], s["longitude"]])
        risk_value = risk(s["risk"], distance, w_amount)
        scores.append(score(a, b, risk_value, distance))
    # greedily chooose minimum score for facility to go to
    min_score = min(scores)
    min_score_idx = scores.index(min_score)
    # return the facility (as a dictionary) that minimizes score
    return sorting[min_score_idx]


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