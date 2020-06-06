import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

print("""
İbrahim Halil Bayat 
Department of Electronics and Communication Engineering 
İstanbul Technical University 
İstanbul, Turkey 
""")

df = pd.read_csv("Car.csv")
print("The Data: \n", df.head())

print("Describing the data: \n", df.describe())
print("\n ----------- Describing Object type values --------------")
print(df.describe(include=['object']))

print("\n------------------- Value Counts for Drive Wheels--------------------")
print(df["drive-wheels"].value_counts())
print("\n------- Framing Drive Wheels -------------")
the_frame = df["drive-wheels"].value_counts().to_frame()
the_frame.rename(columns={'drive-wheels': 'Value-Counts'}, inplace=True)
the_frame.index.name = "drive-wheels"
print(the_frame)

print("\n-------------- Value Counts for Engine Location ----------------------")
print(df["engine-location"].value_counts())
frame_engine_location = df["engine-location"].value_counts().to_frame()
frame_engine_location.rename(columns={'engine-location': "Value-Counts"}, inplace=True)
frame_engine_location.index.name =  "engine-location"
print(frame_engine_location)