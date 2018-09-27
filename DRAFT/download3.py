import  urllib2
for Num in [11,12,13]:
    sNum=str(Num)
    url="https://www.star.nesdis.noaa.gov/smcd/emb/vci/VH/get_provinceData.php?country=UKR&provinceID="+sNum+"&year1=1981&year2=2018&type=Mean"
    vhi_url = urllib2.urlopen(url)
    out = open('vhi_id_'+sNum+'.txt','wb')
    out.write(vhi_url.read())
    out.close()
print "VHI is downloaded..."