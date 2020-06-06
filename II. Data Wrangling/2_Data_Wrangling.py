print("""
İbrahim Halil Bayat 
Department of Electronics and Communication Engineering 
İstanbul Technical University 
İstanbul, Turkey 
""")

import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

filename = "https://s3-api.us-geo.objectstorage.softlayer.net/cf-courses-data/CognitiveClass/DA0101EN/auto.csv"
headers = ["symboling", "normalized-losses", "make", "fuel-type", "aspiration", "num-of-doors", "body-style",
           "drive-wheels", "engine-location", "wheel-base", "length", "width", "height", "curb-weight", "engine-type",
           "num-of-cylinders", "engine-size", "fuel-system", "bore", "stroke", "compression-ratio", "horsepower",
           "peak-rpm", "city-mpg", "highway-mpg", "price"]


df = pd.read_csv(filename, names=headers)
print(df.head())


df.to_csv("raw_auto.csv", index=False)

df.replace("?", np.nan, inplace=True)
print(df.head())

print("\n ----------- Is there any missing data ? -------------")

missing_value = df.isnull()
print(missing_value.head())

print("\n ------------------ Counting Missing values in each column --------------")
for column in missing_value.columns.values.tolist():
    print(column)
    print(missing_value[column].value_counts())
    print("")

print("\n---------- Replacing Normalized Losses -------------")
avg_norm_loss = df['normalized-losses'].astype(float).mean(axis=0)
print("Average of Normalized Losses: ", avg_norm_loss)
df["normalized-losses"].replace(np.nan, avg_norm_loss, inplace=True)
missing_norm_loss = df["normalized-losses"].isnull()
print(missing_norm_loss.value_counts())

print("\n------ Replacing Bore ------------------")
avg_bore = df["bore"].astype(float).mean(axis=0)
df["bore"].replace(np.nan, avg_bore, inplace=True)
missing_bore = df["bore"].isnull()
print(missing_bore.value_counts())

print("\n----------- Replacing Stroke ------------")
avg_stroke = df["stroke"].astype(float).mean(axis=0)
df["stroke"].replace(np.nan, avg_stroke, inplace=True)
missing_stroke = df["stroke"].isnull()
print(missing_stroke.value_counts())

print("\n------------- Replacing Horse Power -----------")
avg_horsepower = df["horsepower"].astype(float).mean(axis=0)
df["horsepower"].replace(np.nan, avg_horsepower, inplace=True)
missing_horsepower = df["horsepower"].isnull()
print(missing_horsepower.value_counts())

print("\n------------- Replacing Peak RPM ---------------")
avg_peak_rpm = df["peak-rpm"].astype(float).mean(axis=0)
df["peak-rpm"].replace(np.nan, avg_peak_rpm, inplace=True)
missing_peak_rpm = df["peak-rpm"].isnull()
print(missing_peak_rpm.value_counts())

print("\n----------------- Replacing Number of Doors with Frequency ------------")
print(df["num-of-doors"].value_counts())
print(df["num-of-doors"].value_counts().idxmax())
df["num-of-doors"].replace(np.nan, "four", inplace=True)
missing_num_of_doors = df["num-of-doors"].isnull()
print(missing_num_of_doors.value_counts())

print("\n----- Dropping Missing Values in Price -----------------")
df.dropna(subset=["price"], axis=0, inplace=True)
df.reset_index(drop=True, inplace=True)
print(df.shape)

print("\n---------- Changing the Types of the Columns -----------")
df[["bore", "stroke"]] = df[["bore", "stroke"]].astype(float)
df[["normalized-losses"]] = df[["normalized-losses"]].astype(int)
df[["price"]] = df[["price"]].astype(float)
df[["peak-rpm"]] = df[["peak-rpm"]].astype(float)

print(df.dtypes)

df.to_csv("cleaned_data.csv", index=False)
print(df.shape)
