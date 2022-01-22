from flask import Flask, request

from parse import parse
from alg import alg
from plot import plot


app = Flask(__name__)

dfs = parse()

# @app.route("/alg/<int:a>/<int:b>/<string:csv_file>")
@app.route("/alg", methods=['GET'])
# def do_alg(a, b, csv_file):
def do_alg():
    args = request.args.to_dict()
    a = args.get('a')
    b = args.get('b')
    csv_file = args.get('csv_file')
    return f'a: {a}, b: {b}, csv_file: {csv_file}'

    a = 0.6
    b = 0.4
    df = dfs[csv_file]
    result = alg(df, a, b)
    return result

print('done')
