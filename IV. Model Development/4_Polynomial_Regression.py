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

def PlotPolly(model, independent_variable, dependent_variable, name):

    x_new = np.linspace(15, 55, 100)
    y_new = model(x_new)

    plt.plot(independent_variable, dependent_variable, '.', x_new, y_new, "-")
    plt.title("Polynomial Fit for Price and Length")
    ax = plt.gca()
    ax.set_facecolor((0.898, 0.898, 0.898))
    fig = plt.gcf()
    plt.xlabel(name)
    plt.ylabel("Price of the cars")

    plt.show()

x = df["highway-mpg"]
y = df["price"]

f = np.polyfit(x, y, 3)
p = np.poly1d(f)
print("The Polynomial: \n", p)

PlotPolly(p, x, y, "highway-mpg")