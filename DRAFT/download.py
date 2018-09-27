import urllib
logo = urllib.urlopen("http://www.google.com/images/srpr/logo3w.png").read()
f = open("logo3w.png", "wb")
f.write(logo)
f.close()