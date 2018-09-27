import itertools as it
import pandas as pd

full_path=('c:/Python27/#Lab1/DOWNLOAD/test.txt') 

def lines_count(str):
	result = len(open(str).readlines())
	return result

#counts lines in file
ll =  lines_count(full_path)
print ll

#upload file to dataframe
names_=["Year","Week","SMN","SMT","VCI","TCI","VHI"]
my_df=pd.read_table(full_path,
	engine="python",
	delimiter="\s+|,\s*",
	index_col=False,
	skipinitialspace=True,
	keep_default_na=False,
	header=None,
	names=names_,
	skiprows=1,
	skipfooter=1) 

size_ = str(my_df.size)

print "read to df complete, size: "+size_ 
print my_df.head(2)
print my_df.tail(2)

#write dataframe to table
my_df.to_excel("out.xls")
