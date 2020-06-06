import numpy as np
import pandas as pd

df = pd.read_csv("cleaned_data.csv")
print("\n--------- Data Transformation o City MPG--------")
print(df.columns)

df["city-L/100km"] = 235/df["city-mpg"]
print(df.head())
print(df.shape)

df["highway-mpg"] = 235/df["highway-mpg"]
df.rename(columns={'highway-mpg': 'highway-L/100km'}, inplace=True)
print(df.columns)

df.to_csv("standardized_data.csv", index=False)