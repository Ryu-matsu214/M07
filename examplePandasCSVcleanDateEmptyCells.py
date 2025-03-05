import pandas as pd

myTable = pd.read_csv("data.csv")

#newMyTable = myTable.dropna()
#myTable.dropna(inplace = True)
#myTable.fillna(5, inplace = True)
myTable["Calories"].fillna(130, inplace = True)

print(myTable.to_string())