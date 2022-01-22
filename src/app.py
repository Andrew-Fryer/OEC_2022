from flask import Flask, request, jsonify

from parse import parse
# from alg import alg
from validator import validator, get_delta_distance
from output import save_file


app = Flask(__name__)

dfs = parse()

@app.route("/list_files", methods=['GET'])
def list_files():
    result = list(dfs.keys())
    print(type(result), result)
    return jsonify(result)

@app.route("/alg", methods=['GET'])
def do_alg():
    args = request.args.to_dict()
    a = args.get('a')
    b = args.get('b')
    csv_file = args.get('csv_file')

    df = dfs[csv_file]

    # run algorithm
    # result = alg(df, a, b)
    solution = df

    solution_file = save_file(solution, csv_file)

    # validate solution
    QoR = validator(csv_file, solution_file)

    # format for front end
    route = []
    prev = None
    for i, row in solution.iterrows():
        if prev == None:
            prev = row
        else:
            id = row['id']
            route.append({
                "startNodeId": prev['id'],
                "endNodeId": row['id'],
                "startLat": prev['latitude'],
                "startLng": prev['longitude'],
                "endLat": row['latitude'],
                "endLng": row['longitude'],
                "distance": get_delta_distance((prev['latitude'], prev['longitude']), \
                    (row['latitude'], row['longitude']))
            })
            prev = row

    return {
        "points": df.to_dict('records'),
        "route": route,
        "data": {
            "totalPlasticProduced": 0,
            "totalPlasticRecycled": 0,
            "totalPlasticLost": 0,
            "totalPlasticInOcean": 0,
            "totalDistance": 0,
            "QoR": QoR,
        },
    }

print('done')
