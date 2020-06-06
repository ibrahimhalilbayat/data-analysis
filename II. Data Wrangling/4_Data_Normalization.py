import numpy as np
import pandas as pd

df = pd.read_csv("standardized_data.csv")

df['length'] = df['length']/df['length'].max()
df["width"] = df['width']/df['width'].max()
df['height'] = df['height']/df['height'].max()

print(df[['length', 'width', 'height']].head())

df.to_csv("normalized_data.csv", index=False)