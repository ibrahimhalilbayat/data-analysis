import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("Binned_Data.csv")
print(df.head())

print("Columns/Features of the Data: \n", df.columns)

print("\n------------- Dummies for Fuel Type --------------------")
dummy_variable_1 = pd.get_dummies(df["fuel-type"])
dummy_variable_1.rename(columns={'diesel': 'fuel-type-diesel', 'gas': 'fuel-type-gas'}, inplace=True)
df = pd.concat([df, dummy_variable_1], axis=1)
df.drop("fuel-type", axis=1, inplace=True)
print("Dummies for Fuel Type are added")

print("\n------------- Dummies for Aspiration -----------------")
dummy_variable_2 = pd.get_dummies(df["aspiration"])
dummy_variable_2.rename(columns={'std': 'aspiration-std', "turbo": "aspiration-turbo"}, inplace=True)
df = pd.concat([df, dummy_variable_2], axis=1)
df.drop("aspiration", axis=1, inplace=True)
print("Dummies for Aspiration are added.")

df.to_csv("Indicated_Data.csv", index=False)

print(df.columns)