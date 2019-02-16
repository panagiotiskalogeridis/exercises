import urllib
webpage=raw_input('give the url of a website (eg.www.somepage.sth)')
f=urllib.urlopen(webpage)
html=f.read()
sub1="</p>"
sub2="<br>"
sub3="href"
a=html.count(sub1)
b=html.count(sub2)
links=html.count(sub3)
linechange=a+b
print linechange, links
