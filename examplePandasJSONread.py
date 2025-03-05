import pandas as pd

myJsonTable = pd.read_json('M07data.json')

print(myJsonTable.to_string())