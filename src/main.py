from parse import parse
from alg import alg
from plot import plot

df = parse()
result = alg(df)
plot(df, result)

print('done')
