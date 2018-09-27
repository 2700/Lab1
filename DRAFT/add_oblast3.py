# -*- coding: utf-8 -*-
import pandas as pd
import numpy as np
import os

print u"Привет!"
#upload source list
source_path = "c:/Python27/#Lab1/Source"
file_1=os.path.join(source_path, "obl_list.txt")
names_df=pd.read_table(file_1, 
	delimiter="\t")
#	index_col=0)
print names_df.head(2)

#upload xls base
file_2="out.xls"
xls_df=pd.read_excel(file_2)
#print xls_df.head(2)

#insert line with province names
xls_df=xls_df.merge(names_df,
	how="left",
	left_on=xls_df(2),
	right_on=names_df(1))
xls_df=xls_df.drop(columns=9)
#xls_df=xls_df[["Province name"] + xls_df.columns[:-1].tolist()]
print xls_df.head(2)

#write dataframe to xls file
xls_df.to_excel("out_names_ru.xls")

