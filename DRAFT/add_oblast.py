# coding: cp1251
import pandas as pd
import os

#upload source list
source_path = "c:/Python27/#Lab1/Source"
file_1=os.path.join(source_path, "obl_list_en.txt")
source_df=pd.read_table(file_1)
print source_df.head(2)

#upload xls base
file_2='out.xls'
xls_df=pd.read_excel(file_2)
print xls_df.head(2)

#insert line with province names
result_df=xls_df.insert(, 3, 99)
