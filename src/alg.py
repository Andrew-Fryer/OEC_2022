from cmath import nan
from threading import local
import numpy as np
import math
import pandas as pd

# csv file, a, b
def alg(df, risk_weight, distance_weight):
    # decide on optimal order for each specific set of waste
    # paths order [[local_sorting_idx, regional_sorting_idx, regional_recycling_idx],...]
    waste_facility = df[df.iloc[:,3].str.equals('waste')]
    waste_facility.reset_index(drop=True, inplace=True)
    local_sorting = df[df.iloc[:,3].str.equals('local_sorting_facility')]
    local_sorting.reset_index(drop=True, inplace=True)
    regional_sorting = df[df.iloc[:,3].str.equals('regional_sorting_facility')]
    regional_sorting.reset_index(drop=True, inplace=True)
    regional_recycling = df[df.iloc[:,3].str.equals('regional_recycling_facility')]
    regional_recycling.reset_index(drop=True, inplace=True)

    waste_facility["next facility"] = -1
    waste_facility["next distance"] = -1
    local_sorting["next facility"] = -1
    local_sorting["next distance"] = -1
    regional_sorting["next facility"] = -1
    regional_sorting["next distance"] = -1
    regional_recycling["using"] = -1

    for idx, row in waste_facility.iterrows():
        # Waste to local sorting
        local_sorting_idx, local_sorting_dist = optimal_facility(row, local_sorting, risk_weight, distance_weight)
        waste_facility["next facility"][idx] = local_sorting_idx
        waste_facility["next distance"][idx] = local_sorting_dist

        # local sorting to regional sorting
        regional_sorting_idx, regional_sorting_dist = optimal_facility(local_sorting.iloc[local_sorting_idx], regional_sorting, risk_weight, distance_weight)
        local_sorting["next facility"][local_sorting_idx] = regional_sorting_idx
        local_sorting["next distance"][local_sorting_idx] = regional_sorting_dist

        # local sorting to regional sorting
        regional_recycling_idx, regional_recycling_dist = optimal_facility(regional_sorting.iloc[regional_sorting_idx], regional_recycling, risk_weight, distance_weight)
        regional_sorting["next facility"][regional_sorting_idx] = regional_recycling_idx
        regional_sorting["next distance"][regional_sorting_idx] = regional_recycling_dist
        regional_recycling["using"][regional_recycling_idx] = "T"

    waste_facility = waste_facility[waste_facility["next facility"] != -1]
    local_sorting = local_sorting[local_sorting["next facility"] != -1]
    regional_sorting = regional_sorting[regional_sorting["next facility"] != -1]
    regional_recycling = regional_recycling[regional_recycling["using"] != -1]

    final_frame = pd.DataFrame(columns=['id', 'latitude', 'longitude','type', 'amount', 'risk'])

    final_frame = ordering(waste_facility, local_sorting, final_frame)
    final_frame = ordering(local_sorting, regional_sorting, final_frame)
    final_frame = ordering(regional_sorting, regional_recycling, final_frame)

    final_frame = final_frame.drop(['next facility', 'next distance', 'using'], axis=1) 
    return final_frame

def get_child_frame(parent_idx, all_possible_children):
    return all_possible_children[all_possible_children.iloc[:,6].eq(parent_idx)]

def ordering(child_frame, parent_frame, order_frame):
    for idx_parent, row_parent in parent_frame.iterrows(): 
        new_child = get_child_frame(idx_parent, child_frame)  # new child frame only with parent in it
        new_frame = shortest_distance_order(new_child)
        order_frame = pd.concat([order_frame, new_frame])
        order_frame = order_frame.append(row_parent, ignore_index=True)

    return order_frame

def shortest_distance_order(frame):
    id_list = []
    last_id = frame[frame["next distance"] == frame["next distance"].min()].iloc[0]["id"]
    # ignoring order
    for idx, row in frame.iterrows():
        if row["id"] != last_id:
            id_list.append(row["id"])
    id_list.append(last_id)

    frame['id'] = pd.Categorical(
        frame['id'],
        categories=id_list,
        ordered=True
    )
    new_frame = frame.sort_values('id')
    return new_frame


def risk(facility_risk, distance_travelled, amount_processing):
    return facility_risk*distance_travelled*amount_processing

# moving waste to local sorting facility 
def optimal_facility(facility1, facility2, a, b):
    scores = []
    distances = []
    for idx, row in facility2.iterrows():
        distance = get_delta_distance([facility1["latitude"], facility1["longitude"]],[row["latitude"], row["longitude"]])
        distances.append(distance)
        risk_value = risk(row["risk"], distance, facility1["amount"])
        scores.append(score(a, b, risk_value, distance))
    # greedily chooose minimum score for facility to go to
    min_score = min(scores)
    min_score_idx = scores.index(min_score)
    # return row index for specfied facility2 dataframe
    return min_score_idx, distances[min_score_idx]


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
alg(df, 0.9, 0.1)
print()
