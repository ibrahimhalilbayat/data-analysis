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

print("\n----------- Unique Values of Drive Wheels ------------")
print(df["drive-wheels"].unique())

print("\n------------- First Group: Drive Wheels, Body Style, and Price ------")
df_group_one = df[["drive-wheels", "body-style", "price"]]
print(df_group_one.head())

df_group_one = df_group_one.groupby(["drive-wheels"], as_index=False).mean()
print("The Group one mean: \n", df_group_one)

df_gptest = df[["drive-wheels", "body-style", "price"]]
grouped_test1 = df_gptest.groupby(["drive-wheels", "body-style"], as_index=False).mean()
print(grouped_test1)

print("\n----------- Pivot Table ---------------")

grouped_pivot = grouped_test1.pivot(index="drive-wheels", columns="body-style")
grouped_pivot.fillna(0, inplace=True)
print(grouped_pivot)

print("\n------------- Grouping based on Price and Body Style ----------------")
the_group = df[["body-style", "price"]]
the_group = the_group.groupby(["body-style"], as_index=False).mean()
print(the_group)

print("\n------------ Plotting Pivot Group: Drive Wheels, Body Style, and Price -----------")
plt.pcolor(grouped_pivot, cmap='RdBu')
plt.colorbar()
plt.title("Plot of Drive Wheels, Body Style, and Price")
plt.show()

fig, ax = plt.subplots()
im = ax.pcolor(grouped_pivot, cmap = 'RdBu')

row_labels = grouped_pivot.columns.levels[1]
col_labels = grouped_pivot.index

ax.set_xticks(np.arange(grouped_pivot.shape[1]) + 0.5, minor=False)
ax.set_yticks(np.arange(grouped_pivot.shape[0]) + 0.5, minor=False)

ax.set_xticklabels(row_labels, minor=False)
ax.set_yticklabels(col_labels, minor=False)

plt.xticks(rotation=90)

fig.colorbar(im)
plt.show()