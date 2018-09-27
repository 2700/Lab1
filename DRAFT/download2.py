import  urllib2
url="https://www.star.nesdis.noaa.gov/smcd/emb/vci/VH/get_provinceData.php?country=UKR&provinceID=11&year1=1981&year2=2018&type=Mean"
open_url = urllib2.urlopen(url)
print(open_url.read())
out = open('vhi_id_11.txt','wb')
out.write(open_url.read())
out.close()
print "VHI is downloaded..."