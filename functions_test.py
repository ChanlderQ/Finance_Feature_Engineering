import pandas as pd
import numpy as np

# test the functions in main files

my_func=my_features_functions()

data=pd.read_csv('data.csv')

indicator1=my_func.p2vol(data.open_price,data.high_price,data.low_price,data.close_price,data.vol)
