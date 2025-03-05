import pandas as pd

myTable = pd.read_csv("data2.csv")

#myTable["Date"] = pd.to_datetime(myTable["Date"])

myTable.dropna(subset=['Date'], inplace = True)
#print(myTable.to_string())

print(myTable.duplicated())

myTable.drop_duplicates(inplace = True)

print(myTable.duplicated())