# Simple Application for bs4 module
import os,bs4,requests as rq
# use bs4 module to analyze html

res = rq.get('http://nostarch.com')
res.raise_for_status()# check the status of connection
noStarchSoup = bs4.BeautifulSoup(res.text,'html.parser')
print(type(noStarchSoup))

exampleFile = open(os.path.join(os.getcwd(),'example.html'))
# read from local html file
exampleSoup = bs4.BeautifulSoup(exampleFile,'html.parser')
print(type(exampleSoup))

#use select() to search element
elems = exampleSoup.select('#author')#return list of Tag Object
print(len(elems))
print(type(elems))

print(elems[0].getText())# print content in the tag object
print(str(elems[0]))# print with full label
print(elems[0].attrs)# print attribute of the tag object
print(elems[0].get('id'))#use get() to get the attribute of the tag object