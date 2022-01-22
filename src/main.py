from parse import parse
from alg import alg
from plot import plot
from validator import validator, get_delta_distance
from output import save_file


a = 0.6
b = 0.4

csv_file_name = "test_10_equal.csv"

QoR = validator("data/small/test_10_equal", "output/test_10_equal", a, b)

print('done')
