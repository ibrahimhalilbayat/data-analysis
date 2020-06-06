import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
import seaborn as sns

print("""
İbrahim Halil Bayat 
Department of Electronics and Communication Engineering 
İstanbul Technical University 
İstanbul, Turkey 
""")

df = pd.read_csv("car.csv")

plt.figure(figsize=(12, 10))
sns.regplot(x="highway-mpg", y="price", data=df)
plt.ylim(0,)
plt.title("Regression Plot for Highway Mpg and Price")
plt.show()

sns.regplot(x="peak-rpm", y="price", data=df)
plt.ylim(0,)
plt.title("Regression Plot for Peak RPM and the Price")
plt.show()