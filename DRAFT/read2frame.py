import pandas
aDataFrame = pandas.read_table('./DOWNLOAD/vhi_id_11.txt', delim_whitespace=True, names=('Year', 'Week', 'CCC','SMN','SMT','VCI','TCI','VHI'))
aDataFrame.to_csv('result.csv', index=False)


#from pandas import DataFrame
#import pandas
#import os
#
#def get_file_name( path):
#    return os.path.basename(path).split(".")[0].strip().lower() 
#
#name = get_file_name('./inputs/dist.txt')
#with open('./inputs/dist.txt') as f:
#    vDataFrame = DataFrame(0.0, index=[1,2,3], columns=[1,2,3])
#    for line in f:
#        data = line.strip().split()
#        row,column,value = [int(i) if i.isdigit() else float(i) for i in data]
#        df.set_value(row,column,value)
#m[name] = vDataFrame 