import  urllib2
import datetime
iCounter = int(0)
for Num in range(11,13):
    iCounter += 1
    sNum=str(Num)
    now = datetime.datetime.now()
    sDate=str(now.strftime("%d-%m-%Y_%Hh%Mm"))
    url="https://www.star.nesdis.noaa.gov/smcd/emb/vci/VH/get_provinceData.php?country=UKR&provinceID="+sNum+"&year1=2008&year2=2018&type=Mean"
    vhi_url = urllib2.urlopen(url)
    out = open('vhi_id_'+sNum+'_'+sDate+'.txt','wb')
    out.write(vhi_url.read())
    out.close()
sCounter=str(iCounter)
sResultTxt="There are "+sCounter+" VHI's downloaded..."
print sResultTxt 