import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

print("""
İbrahim Halil Bayat 
Department of Electroncis and Communication Engineering 
İstanbul Technical University 
İstanbul, Turkey 
""")

df = pd.read_csv("Car.csv")
print("What the the has at first 5 rows: \n", df.head())

print("Types of my data: \n", df.dtypes)

print("The Correlation: \n", df.corr())

print("The correlation between Bore, Stroke, Compression Ration and Horsepower: \n",
      df[["bore", "stroke", "compression-ratio", "horsepower"]].corr())

print("\n--------- Scatter Plot for Engine Size and Price ------------------")
print("Correlation: \n", df[["engine-size", "price"]].corr())
print("Strong Correlation")
sns.regplot(x="engine-size", y="price", data=df)
plt.ylim(0,)
plt.title("Regression Plot for Engine Size and Price")
plt.show()

print("\n------------ Scatter Plot for Peak-RPM and Price -------------------")
print("Correlation: \n", df[["peak-rpm", "price"]].corr())
print("Weak Correlation")
sns.regplot(x="peak-rpm", y="price", data=df)
plt.ylim(0,)
plt.title("Regression Plot for Peak-RPM and Price")
plt.show()

print("\n--------------- Scatter Plot for Stroke and Price -------------------")
print("Correlation: \n", df[["stroke", "price"]].corr())
print("Weak Correlation")
sns.regplot(x="stroke", y="price", data=df)
plt.ylim(0,)
plt.title("Regression Plot for Stroke and Price")
plt.show()
