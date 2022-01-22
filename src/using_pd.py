import pandas as pd

df = pd.read_csv("./provided/small/test_10_equal.csv",header=None,names = ['id','latitude','longitude','type','amount','risk'])

waste = df[df.iloc[:,3].str.contains('waste')]
local_sorting = df[df.iloc[:,3].str.contains('local_sorting_facility')]
regional_sorting = df[df.iloc[:,3].str.contains('regional_sorting_facility')]
regional_recycling = df[df.iloc[:,3].str.contains('regional_recycling_facility')]

print(local_sorting)

