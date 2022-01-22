from flask import Flask, request, jsonify

from parse import parse
from alg import alg


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
    result = alg(df, a, b)

    return {}

print('done')
