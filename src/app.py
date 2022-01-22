from flask import Flask, request, jsonify
import os

from parse import parse
from alg import alg
from validator import validator, get_delta_distance
from output import save_file
# from evaluator import evaluate


app = Flask(__name__)

dfs, file_to_path = parse()

@app.route("/list_files", methods=['GET'])
def list_files():
    result = list(dfs.keys())
    print(type(result), result)
    return jsonify(result)

@app.route("/alg", methods=['GET'])
def do_alg():
    args = request.args.to_dict()
    a = float(args.get('a'))
    b = float(args.get('b'))
    csv_file_name = args.get('csv_file')

    df = dfs[csv_file_name]
    csv_file = file_to_path[csv_file_name]

    # run algorithm
    solution = alg(df, a, b)

    solution_file = save_file(solution, csv_file_name)

    # validate solution
    def without_ext(f):
        return os.path.splitext(f)[0]
    print(without_ext(csv_file), without_ext(solution_file), a, b)
    QoR, total_distance, total_plastic_lost = validator(without_ext(csv_file), without_ext(solution_file), a, b)

    # format for front end
    route = []
    prev = None
    # total_distance = 0
    for i, row in solution.iterrows():
        if prev is None:
            prev = row
        else:
            distance = get_delta_distance(\
                (prev['latitude'], prev['longitude']), \
                (row['latitude'], row['longitude'])
            )
            route.append({
                "startNodeId": prev['id'],
                "startLat": prev['latitude'],
                "startLng": prev['longitude'],
                "startType": prev['type'],
                "endNodeId": row['id'],
                "endLat": row['latitude'],
                "endLng": row['longitude'],
                "endType": row['type'],
                "distance": distance,
            })
            # total_distance += distance
            prev = row

    return {
        "points": df.to_dict('records'),
        "route": route,
        "data": {
            "totalPlasticProduced": 0,
            "totalPlasticRecycled": 0,
            "totalPlasticLost": total_plastic_lost,
            "totalPlasticInOcean": total_plastic_lost,
            "totalDistance": total_distance,
            "QoR": QoR,
        },
    }

print('done')
