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

df_gptest = df[['drive-wheels', 'body-style', 'price']]

grouped_test2 = df_gptest[["drive-wheels", "price"]].groupby(["drive-wheels"])
print(grouped_test2.head())
print("-----------------------------------------------------")
print("Grouping based on '4wd': \n", grouped_test2.get_group('4wd')['price'])

print("ANOVA: ")
f_val, p_val = stats.f_oneway(grouped_test2.get_group('fwd')['price'], grouped_test2.get_group('rwd')['price'],
                              grouped_test2.get_group('4wd')['price'])

print("ANOVA results: F=", f_val, ", P =", p_val)
