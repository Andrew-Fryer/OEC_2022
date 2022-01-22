from parse import parse
from alg import alg
from plot import plot

a = 0.6
b = 0.4

dfs = parse()
df = dfs["test_10_equal.csv"]
result = alg(df, a, b)
plot(df, result)

print('done')
