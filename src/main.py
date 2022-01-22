from flask import Flask

from parse import parse
from alg import alg
from plot import plot

app = Flask(__name__)

@app.route("/alg/<int:a>/<int:b>/<string:csv_file>")
def do_alg(a, b, csv_file):
    return f'a: {a}, b: {b}, csv_file: {csv_file}'


a = 0.6
b = 0.4

dfs = parse()
df = dfs["test_10_equal.csv"]
result = alg(df, a, b)
plot(df, result)

print('done')
