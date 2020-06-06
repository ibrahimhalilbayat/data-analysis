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
lr = LinearRegression()

plt.figure(figsize=(12, 10))
sns.residplot(x="highway-mpg", y="price", data=df)
plt.title("Residual Plot for Highway Mpg and the Price")
plt.show()

z = df[['horsepower', 'curb-weight', 'engine-size', 'highway-mpg']]

lr.fit(z, df["price"])
yhat = lr.predict(z)

ax1 = sns.distplot(df["price"], hist=False, color='r', label="Actual Values")
sns.distplot(yhat, hist=False, color='b', label="Predicted Values", ax=ax1)

plt.xlabel("Price in dollars")
plt.ylabel("Proportion of the cars")
plt.title("Actual vs Predicted values")
plt.show()