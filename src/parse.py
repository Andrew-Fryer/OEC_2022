import pandas as pd
import numpy as np
import os
from glob import glob

def parse():
    # files = glob("provided/**/*.csv")
    df = pd.read_csv("provided/small/test_10_equal.csv", \
        names=['ID', 'Latitude', 'Longitude', 'Type', 'Amount', 'Risk'])

    return {
        "test_10_equal.csv": df
    }
