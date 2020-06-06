import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
import seaborn as sns
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler
from sklearn.preprocessing import PolynomialFeatures

print("""
İbrahim Halil Bayat 
Department of Electronics and Communication Engineering 
İstanbul Technical University 
İstanbul, Turkey 
""")

df = pd.read_csv("car.csv")

Input=[('scale',StandardScaler()), ('polynomial', PolynomialFeatures(include_bias=False)),
       ('model',LinearRegression())]

pipe = Pipeline(Input)
print("The Pipeline: \n", pipe)

z = df[['horsepower', 'curb-weight', 'engine-size', 'highway-mpg']]
y = df["price"]

pipe.fit(z, y)

y_piped = pipe.predict(z)
print("First 5 values of predicted values: \n", y_piped[0:5])