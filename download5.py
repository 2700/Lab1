import urllib2
import datetime
import os.path

py_dir = os.path.dirname(os.path.abspath(__file__))
work_dir = os.path.join("DOWNLOAD")
iCounter = int(0)
for Num in range(1,28):
    iCounter += 1
    sNum=str(Num)
    vNow = datetime.datetime.now()
    sDate=str(vNow.strftime("%d-%m-%Y_%Hh%Mm"))
    url="https://www.star.nesdis.noaa.gov/smcd/emb/vci/VH/get_provinceData.php?country=UKR&provinceID="+sNum+"&year1=1981&year2=2018&type=Mean"
    target_url = urllib2.urlopen(url)
    file_name = "vhi_id_"+sNum+"_"+sDate+".txt"
    full_path = os.path.join(py_dir, work_dir, file_name)
    work_file = open(full_path,"w")
    work_file.write(target_url.read())
    work_file.close()
		
sResultTxt="There are "+str(iCounter)+" files downloaded..."
print sResultTxt
