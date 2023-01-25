import pandas as pd
import numpy as np

data=pd.read_csv("data.csv")

func_list=["p2vol","low2high"]
my_fea=feature_engineering(func_list,rolling_window=10)
output_feature=my_fea.output_feature(data)
