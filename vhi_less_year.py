import pandas as pd
import numpy as np
import os

result_path ="C:/Python27/#Lab1/RESULT" 
file_=os.path.join(result_path,"out+names.xls")

df=pd.read_excel(file_)
pt=pd.pivot_table(df[df.VHI < 35],
	index=["Year","Province name"],
	values=["VHI"],
	aggfunc="count")
pt=pt.sort_values(by=["VHI"], ascending=False)
print pt.head(10)
#pt.to_excel("PIVOT/pivot_table_year.xls")