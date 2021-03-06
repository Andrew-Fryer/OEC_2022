from cmath import nan
from threading import local
import numpy as np
import math
import pandas as pd
import warnings
warnings.filterwarnings("ignore")

# csv file, a, b
def alg(df, risk_weight, distance_weight):
    # decide on optimal order for each specific set of waste
    # paths order [[local_sorting_idx, regional_sorting_idx, regional_recycling_idx],...]
    waste_facility = df[df.iloc[:,3].str.contains('waste')]
    waste_facility.reset_index(drop=True, inplace=True)
    local_sorting = df[df.iloc[:,3].str.contains('local_sorting_facility')]
    local_sorting.reset_index(drop=True, inplace=True)
    regional_sorting = df[df.iloc[:,3].str.contains('regional_sorting_facility')]
    regional_sorting.reset_index(drop=True, inplace=True)
    regional_recycling = df[df.iloc[:,3].str.contains('regional_recycling_facility')]
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
    waste_facility.drop(index=waste_facility.index[0], axis=0, inplace=True)
    order = ordering(waste_facility, local_sorting, [0])
    order = ordering(local_sorting, regional_sorting, order)
    order = ordering(regional_sorting, regional_recycling, order)

    # print('here')
    final_data = []
    for i in order:
        final_data.append(df.loc[i])
    final_frame = pd.DataFrame(final_data, columns=['id', 'latitude', 'longitude','type', 'amount', 'risk'])
    # print('now here')
    return final_frame

def get_child_frame(parent_idx, all_possible_children):
    return all_possible_children[all_possible_children.iloc[:,6].eq(parent_idx)]

def ordering(child_frame, parent_frame, order):
    for idx_parent, row_parent in parent_frame.iterrows(): 
        shortest_distance = None
        shortest_distance_id = 0
        for idx_child, row_child in child_frame.iterrows():
            if idx_parent == row_child['next facility']:
                if shortest_distance == None or shortest_distance > row_child['next distance']:
                    if shortest_distance != None: 
                        order.append(shortest_distance_id)
                    shortest_distance = row_child['next distance']
                    shortest_distance_id = row_child['id']
                else:
                    order.append(row_child['id'])
        order.append(shortest_distance_id)
        order.append(row_parent['id'])
    

    return order

def shortest_distance_order(frame):
    id_list = []
    last_id = frame[frame["next distance"] == frame["next distance"].min()].iloc[0]["id"]
    # ignoring order
    for idx, row in frame.iterrows():
        if row["id"] != last_id:
            id_list.append(row["id"])
    id_list.append(last_id)

    frame['id'] = pd.Categorical(frame['id'], categories=id_list, ordered=True)
    frame.sort_values('id', inplace = True)
    return frame


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
    latavg = (int(x1_lat) + int(x2_lat))/2

    x1 = R * int(y1_lon) * math.cos(latavg)
    y1 = R * int(x1_lat)

    x2 = R * int(y2_lon) * math.cos(latavg)
    y2 = R * int(x2_lat)

    return math.hypot(abs(x1-x2), abs(y1-y2))/1000


# df = pd.read_csv("./data/small/test_100_recycle.csv",header=None,names = ['id','latitude','longitude','type','amount','risk'])
# id_order = alg(df, 1, 1)
# print(id_order)
