#use requests module to download file of webpage and store it in hard disk 
import requests
res = requests.get('https://automatetheboringstuff.com/files/rj.txt')
res.raise_for_status()#check the status of the connection
textFile = open("RomeoAndJuliet.txt","wb") #'wb' -> write binary

for chunk in res.iter_content(100000):#chunk size: 100000 bytes for each
    #regard data of res as many chunks and use function iter_content() to read it
    textFile.write(chunk)#write content into the textFile

textFile.close()