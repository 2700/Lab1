import itertools as it
import pandas as pd
import os

dir_path=("c:/Python27/#Lab1/DOWNLOAD/") 
base_df=pd.DataFrame([])
for counter_, filename in enumerate(os.listdir(dir_path)):
	full_path=(os.path.join(dir_path,filename))
	if filename.endswith(".txt"): 
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

		#add a new column
		my_df.insert(0, "Region", str_2, allow_duplicates=False)
		
		#print result
		size_str = str(my_df.size)
		counter_str=str(counter_)
		print "read file #"+counter_str+" to df complete, size: "+size_str
#		print my_df.head(2)
#		print my_df.tail(2)
		base_df=base_df.append(my_df)
#		print my_df.head(2)

#write dataframe to table
base_df.to_excel("RESULT/out.xls")
