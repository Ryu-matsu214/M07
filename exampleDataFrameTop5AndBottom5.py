import pandas as pd

myTable = pd.read_csv("data.csv")

print(myTable.head())
print()
print(myTable.tail())
print()
print(myTable.info())