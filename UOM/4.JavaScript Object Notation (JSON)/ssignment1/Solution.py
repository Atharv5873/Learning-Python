import urllib.request, urllib.parse, urllib.error
import json
import ssl

api_key= False
serviceurl='http://maps.googleapis.com/maps/api/geocode/xml?'

url=input('Enter location: ')
print('Retriving ',url)
uh=urllib.request.urlopen(url)
data=uh.read()
print('Retrived',len(data),'characters')

js=json.loads(data)
info=js["comments"]

sum=0
print('Count: ',len(info))
for i in info:
    sum+=int(i['count'])
print('Sum:',sum)    