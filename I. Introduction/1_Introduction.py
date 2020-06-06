print("""
İbrahim Halil Bayat 
Department of Electronics and Communication Engineering 
İstanbul Technical University 
İstanbul, Turkey 
""")

import pandas as pd

# Path for Data URL
url_path = "https://s3-api.us-geo.objectstorage.softlayer.net/cf-courses-data/CognitiveClass/DA0101EN/auto.csv"

# Data has no header. So;
df = pd.read_csv(url_path, header=None)

print("Data without a header: \n", df.head())

# We need a header list as the columns/features
headers = ["symboling", "normalized-losses", "make", "fuel-type", "aspiration", "num-of-doors", "body-style",
           "drive-wheels", "engine-location", "wheel-base", "length", "width", "height", "curb-weight", "engine-type",
           "num-of-cylinders", "engine-size", "fuel-system", "bore", "stroke", "compression-ratio", "horsepower",
           "peak-rpm", "city-mpg", "highway-mpg", "price"]

print("The Headers / Features / Columns of the Data: \n", headers)

print("\n------------- Adding headers to the data ----------------")

df.columns = headers

print("\nFirst 5 rows of the data with the header: \n", df.head())

print("\nLast 5 rows of the data with the header: \n", df.tail())

print("""
If there are missing values in Price feature. 
We can drop them with 'df.dropna()'
""")

df['price'].dropna(axis=0)

print("\n----------- Saving the Data with 'df.to_csv()' ------------")
df.to_csv("automobile.csv", index=False)
print("Saving the data as 'automobile.csv'")

print("\n ----------------------- Types of the Features with 'df.dtypes'  -----------------")

print(df.dtypes)

print("\n ------------------ Describing the Data with 'df.describe()' ---------------")
print(df.describe(include='all'))

print("\n -------------------- Describing specific columns ------------------------")

print(df[['make', 'city-mpg', 'price']].describe(include='all'))

print("\n ----------------- Information about the data with 'df.info()' ------------")
print(df.info())
