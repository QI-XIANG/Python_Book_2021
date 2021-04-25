# Special Topic: Download some comic image from XKCD (https://xkcd.com/)
import requests as rq,bs4,os
url = 'https://xkcd.com/'
os.makedirs('xkcd',exist_ok=True) # exist_ok=True -> prevent error happened when the folder had existed

while not url.endswith('#'):
    #download the page
    print('Downloading page %s' % url)
    res = rq.get(url)
    res.raise_for_status()# check the status of the connection

    soup = bs4.BeautifulSoup(res.text,'html.parser')

    #find the url of the comic image
    comicElems = soup.select('#comic img')
    if comicElems == []:
        print('Could not find comic image.')
    else:
        try:
            comicUrl = 'http:'+comicElems[0].get('src')
            #download image
            print('Downloading img %s' % comicUrl)
            res = rq.get(comicUrl)
            res.raise_for_status()
        except rq.exceptions.MissingSchema:
            #skip the comic
            prevLink = soup.select('a[rel="prev"]')[0]
            url = 'https://xkcd.com/'+prevLink.get('href')
            continue
    #Save comic image to ./xkcd
    imageFile = open(os.path.join('xkcd',os.path.basename(comicUrl)),'wb')
    for chunk in res.iter_content(100000):
        imageFile.write(chunk)
    imageFile.close()
    #Get the prev buttons's url
    prevLink = soup.select('a[rel="prev"]')[0]
    url = 'https://xkcd.com/'+prevLink.get('href')

print('Done')
 