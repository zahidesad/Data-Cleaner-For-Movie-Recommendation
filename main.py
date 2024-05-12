import numpy as np
import pandas as pd
from MissingValueHandler import MissingValueHandler
from OutlierHandler import OutlierHandler

df = pd.read_csv("synthetic_sample_data.csv")

print("Before missing value handler")
print(df.loc[118, "Budget in USD"])

mv_handler = MissingValueHandler(strategy="constant", constant_value=100)
# Remove the first column(unnamed column)
df = mv_handler.remove_column(df, df.columns[0])
df = mv_handler.fit_transform(df, "Budget in USD")
print(df)

print("After missing value handler")
print(df.loc[118, "Budget in USD"])

data = pd.DataFrame({
    'A': [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 1000]
})

print("Before outlier handling\n")
print(data)

handler = OutlierHandler(threshold=1.5)
data_cleaned = handler.fit_transform(data, 'A')

print("After outlier handling\n")
print(data_cleaned)
