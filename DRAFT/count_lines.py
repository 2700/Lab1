from pandas import read_csv
full_path=('c:/Python27/#Lab1/DOWNLOAD/test.txt') 

def lines_count(str):
	result = len(open(str).readlines())
	return result

print lines_count(full_path)
print full_path.readlines(2)
df = read_csv(full_path,
		sep=" ",
		names=["1","2","3","4","5","6","7"],
		).replace(","," ")
df.to_csv('out.csv')



     
	
