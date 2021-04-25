# Simple Application for requests module
import requests
# use requests.get() to download webpage
res = requests.get('https://automatetheboringstuff.com/files/rj.txt')
type(res)

#check connection status
print(res.status_code == requests.codes.ok)

#get length for the text in the webpage
print(len(res.text))
print(res.text[:250])#print some content

#detection error 
res.raise_for_status() #If the connection error happened, thrown exception. Do nothing when no error happened.

res = requests.get('https://inventwithpython.com/page_that_does_not_exist')
try:
    res.raise_for_status()
except Exception as exc:
    print('There was a problem: %s' % (exc))


