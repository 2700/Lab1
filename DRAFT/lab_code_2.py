import pandas as pd
df = pd.read_csv('c:/Python27/#Lab1/Download/test.txt',
		index_col=False, header=0)
print list(df.columns.values)
print df[:1]
