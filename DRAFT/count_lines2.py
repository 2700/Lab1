from pandas import read_csv
full_path=('c:/Python27/#Lab1/DOWNLOAD/test.txt') 

def lines_count(str):
	result = len(open(str).readlines())
	return result

ll =  lines_count(full_path)
source_file = open(full_path, "r")
# use readline() to read the first line 
line = source_file.readline()
while line:
	str1 = line.replace(","," ")
	str2 = str1.replace("   ","  ")
        str3 = str2.replace("  "," ")
        print str3\n
	line = source_file.readline()
source_file.close