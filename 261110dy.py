import pandas as pd
import numpy as np

df = pd.read_csv('data/13_diecasting_small.csv')
hy = df['형체력']
print(hy.head(3))
# 0    258.0
# 1    257.0
# 2    253.0
# Name: 형체력, dtype: float64
print(df[['형체력', '실린더압력']].shape)
print(df[['형체력', '실린더압력']].dtypes)
print(df[['형체력']].dtypes)