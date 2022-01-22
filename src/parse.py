import pandas as pd
import numpy as np
import os
from glob import glob

def parse():
    files = glob("../data/**/*.csv")
    dfs = {}

    for f in files:
        df = pd.read_csv(f, \
            names=['id', 'latitude', 'longitude', 'type', 'amount', 'risk'])

        file_name = os.path.basename(f)
        if dfs.get(file_name):
            print("warning!; duplicate file names (in different directories)")
        dfs[file_name] = df
    return dfs
