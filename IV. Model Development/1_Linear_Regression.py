import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression

print("""
İbrahim Halil Bayat 
Department of Electronics and Communication Engineering 
İstanbul Technical University 
İstanbul, Turkey 
""")

df = pd.read_csv("car.csv")
print("Head of the data: \n", df.head())

lr = LinearRegression()

x = df[['highway-mpg']]
y = df['price']

lr.fit(x, y)

yhat = lr.predict(x)
print("First five predicted values: \n", yhat[0:5])
print("Intercept of the Model: ", lr.intercept_)
print("Slope of the model: ", lr.coef_)

print("\n-------------- Multiple Linear Regression ---------------")

z = df[['horsepower', 'curb-weight', 'engine-size', 'highway-mpg']]

lr.fit(z, df['price'])
print("Intercept for Multiple Linear Regression: ", lr.intercept_)
print("Coefficients of the Multiple Linear Regression: ", lr.coef_)
