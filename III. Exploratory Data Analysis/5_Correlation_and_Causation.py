import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
from scipy import stats

print("""
İbrahim Halil Bayat 
Department of Electronics and Communication Engineering 
İstanbul Technical University 
İstanbul, Turkey 
""")

df = pd.read_csv("Car.csv")
print("--------------------- The Correlation: ---------------------\n", df.corr())

print("\n------------------- Pearson Correlation between Wheel Base and Price ------------")
pearson_coef, p_value = stats.pearsonr(x=df["wheel-base"], y=df["price"])
print("The Pearson Coefficient: {}, The P_Value: {}".format(pearson_coef, p_value))

