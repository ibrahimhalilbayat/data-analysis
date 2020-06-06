import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("normalized_data.csv")

categorical_list = ['make', 'fuel-type', "aspiration", 'num-of-doors', 'body-style', 'drive-wheels',
                    'engine-location', 'engine-type', 'num-of-cylinders', 'fuel-system']

plt.hist(df["horsepower"])
plt.xlabel("Horse Power")
plt.ylabel("Count")
plt.title("Horse Power Histogram")
#plt.show()

bins_horse_power = np.linspace(df["horsepower"].min(), df["horsepower"].max(), 4)
print("The Bin Boundaries: ", bins_horse_power)
bins_names = ['Low', 'Medium', 'High']

df["binned-horsepower"] = pd.cut(df["horsepower"], bins_horse_power, labels=bins_names, include_lowest=True)
print(df["binned-horsepower"].head())
print(df["binned-horsepower"].value_counts())

plt.hist(df["binned-horsepower"], bins=3)
plt.xlabel("Bins")
plt.ylabel("Count")
plt.title("Binned Horse Power")
#plt.show()

print(df["make"].value_counts())

df.to_csv("Binned_Data.csv", index=False)