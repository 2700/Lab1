import itertools as it
import pandas as pd

full_path=('c:/Python27/#Lab1/DOWNLOAD/vhi_id_1_22-06-2018_02h27m.txt') 

#get region num from file
target_file = open(full_path, "r")
str_1 = target_file.readline()
target_file.close()
str_2=str_1[29:31].replace(":","")

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

#add a new column
my_df.insert(0, "Region", str_2, allow_duplicates=False)

print "read to df complete, size: "+size_ 
print my_df.head(2)
print my_df.tail(2)

#write dataframe to table
my_df.to_excel("out.xls")
