from pandas import read_csv
#from pandas import append
from pandas import DataFrame
from itertools import islice

full_path=('c:/Python27/#Lab1/DOWNLOAD/test.txt') 

def lines_count(str):
	result = len(open(str).readlines())
	return result

#counts lines in file
ll =  lines_count(full_path)

#creates empy dataframe with column names
my_df = DataFrame(columns=list('ABCDEFG'))
#reads line by line, clears comas and slashes
with open(full_path) as source_file:
	for line in islice (source_file,2,ll-1):
		str1 = line.replace(","," ")
		str2 = str1.replace("   ","  ")
        	str3 = str2.replace("  "," ")
        	temp_df = DataFrame(str, columns=list('ABCDEFG'))
		my_df = my_df.append(str3)


source_file.close