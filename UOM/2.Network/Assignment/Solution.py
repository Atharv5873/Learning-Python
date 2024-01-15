import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
import ssl

ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input('Enter URL: ')
count=int(input('Enter count: '))
position=int(input('Enter position: '))
print('Retrieving: ',url)

for i in range(count):
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'}
    req = urllib.request.Request(url, headers=headers)

    html = urllib.request.urlopen(req, context=ctx).read()
    soup = BeautifulSoup(html, 'html.parser')

    list=[]
    tags=soup('a')
    for tag in tags:
        list.append(tag.get('href', None))
    url=list[position-1]
    print('Retrieving: ',url)
    


