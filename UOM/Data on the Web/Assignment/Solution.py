import urllib.request, urllib.parse, urllib.error
import xml.etree.ElementTree as ET


api_key = False
serviceurl = 'http://maps.googleapis.com/maps/api/geocode/xml?'


url=input('Enter location: ')
print('Retrieving ',url)
uh = urllib.request.urlopen(url)
data = uh.read()
print('Retrived ',len(data),' characters')

tree=ET.fromstring(data)
counts = tree.findall('.//count')
print('Count: ',len(counts))
sum=0
for n in counts:
    sum+=int(n.text)
print('Sum: ',sum)
