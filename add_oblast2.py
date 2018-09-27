# coding: cp1251
import pandas as pd
import numpy as np
import os

#upload source list
source_path = "C:/Python27/#Lab1/Source"
file_1=os.path.join(source_path, "obl_list_en.txt")
names_df=pd.read_table(file_1, 
	delimiter="\t")
#	index_col=0)
print names_df.head(2)

#upload xls base
result_path ="C:/Python27/#Lab1/RESULT" 
file_2=os.path.join(result_path,"out.xls")
xls_df=pd.read_excel(file_2)
#print xls_df.head(2)

#insert line with province names
xls_df=xls_df.merge(names_df,
	how="left",
	left_on="Region",
	right_on="ID")
xls_df=xls_df.drop(columns="ID")
#xls_df=xls_df[["Province name"] + xls_df.columns[:-1].tolist()]
print xls_df.head(2)

#write dataframe to xls file
xls_df.to_excel("RESULT/out+names.xls")

