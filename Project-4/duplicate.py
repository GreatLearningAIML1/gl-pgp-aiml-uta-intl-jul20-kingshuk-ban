import numpy as np
import pandas as pd


data = dict()
data = {'a': [1, 2, 2, 4, 5, 6, 6], 'b': [1, 2, 2, 4, 5, 6, 6]}
df = pd.DataFrame.from_dict(data, orient='columns')

print(df.head(10))
print("Duplicated row")
print(df[df.duplicated()])
df.drop_duplicates(inplace=True)
print(df.head(10))
