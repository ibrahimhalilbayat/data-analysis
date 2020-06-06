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

sns.boxplot(x="body-style", y="price", data=df)
plt.title("Box Plot for Body Style and Price")
plt.show()

sns.boxplot(x="engine-location", y="price", data=df)
plt.title("Box Plot for Engine Location and Price")
plt.show()

sns.boxplot(x="drive-wheels", y="price", data=df)
plt.title("Box Plot for Drive Wheels and Price")
plt.show()