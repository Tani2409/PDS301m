import pandas as pd
import csv
import os
# data = {
#     'Name': ['Alice', 'Bob', 'Charlie', 'David'],
#     'Age': [24, 30, 22, 35],
#     'City': ['New York', 'Los Angeles', 'Chicago', 'Houston']
# }

# df = pd.DataFrame(data, index=['R1', 'R2', 'R3', 'R4'])
# print(df)

# data1 = [
#     ['Frank', 33, 'Seattle'],
#     ['Alice', 27, 'Boston']
# ]
# column = ['Name', 'Age', 'City']
# row = ['R5', 'R6']
# df1 = pd.DataFrame(data1, index=row, columns=column)
# print(df1)

# with open("data.csv", mode="w", newline="", encoding="utf-8") as f:
#     writer = csv.writer(f)
#     writer.writerow(column)
#     writer.writerows(data1)

# print("Data written to data.csv")

os.chdir(r"C:\Users\ADMIN\Documents\GitHub\PDS301m\class\theory")
df= pd.read_csv("worldwired_tour.csv")
# print(df)
print(df.head(3))  # First 3 rows
print(df.tail(2))  # Last 2 rows
df.info()
print(df.describe())
print(df.shape)
print(df.columns)
print(df.index)
pd.concat([df.head(20), df.tail(20)])

df = pd.read_csv("worldwired_tour.csv", na_values={
'price':["?","n.a"],
'stroke':["?","n.a"],
'horsepower':["?","n.a"],
'peak-rpm':["?","n.a"],
'average-mileage':["?","n.a"]})
print (df)
