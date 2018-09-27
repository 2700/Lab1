import pandas as pd
import numpy as np
import os

result_path ="C:/Python27/#Lab1/RESULT" 
file_=os.path.join(result_path,"out+names.xls")

df=pd.read_excel(file_)
pt=pd.pivot_table(df,
	index=["Region","Year"],
	values=["VHI"],
	aggfunc=[np.min, np.max])
#mmin=xls_df.min()
#mmax=xls_df.max()
#pivot_df[(xls_df['year']==2000) & (xls_df['week']==18)]
#print pt.head(5)
pt.to_excel("PIVOT/pivot_table_min_max.xls")