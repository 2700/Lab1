from pandas import read_csv
from itertools import islice
full_path=('c:/Python27/#Lab1/DOWNLOAD/test.txt')
with open(full_path) as lines:
    for line in islice (lines,1,5):
	print line
fo.close()

#df1 = read_csv("df1.txt")
#df2 = read_csv("df2.txt",";")