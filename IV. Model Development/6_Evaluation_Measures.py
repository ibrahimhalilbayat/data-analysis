import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
import seaborn as sns
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler
from sklearn.preprocessing import PolynomialFeatures
from sklearn.metrics import mean_squared_error

print("""
İbrahim Halil Bayat 
Department of Electronics and Communication Engineering 
İstanbul Technical University 
İstanbul, Turkey 
""")

df = pd.read_csv("car.csv")

lr = LinearRegression()

x = df[["highway-mpg"]]
y = df["price"]

lr.fit(x, y)

print("The R score of the model: ", lr.score(x, y))

yhat = lr.predict(x)
print("The first 5 predicted values are: \n", yhat[0:5])

mse = mean_squared_error(df["price"], yhat)
print("The Mean Squared Error: ", mse)

new_input=np.arange(1, 100, 1).reshape(-1, 1)

predicted_values = lr.predict(new_input)

plt.plot(new_input, predicted_values)
plt.show()
