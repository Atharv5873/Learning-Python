import urllib.request, urllib.parse, urllib.error
import json
import ssl

api_key = False

# If you have a Google Places API key, enter it here
# api_key = 'AIzaSy___IDByT70'
# https://developers.google.com/maps/documentation/geocoding/intro

if api_key is False:
    api_key = 42
    serviceurl = 'http://py4e-data.dr-chuck.net/json?'
else:
    serviceurl = 'http://py4e-data.dr-chuck.net/json?'

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE
address = input('Enter location: ')

parms = dict()
parms['address'] = address
if api_key is not False:
    parms['key'] = api_key
url = serviceurl + urllib.parse.urlencode(parms)
print('Retrieving', url)
uh=urllib.request.urlopen(url,context=ctx)
data=uh.read().decode()
print('Retrived',len(data),'characters')
js=json.loads(data)
place_id=js["results"][0]['place_id']
print('Place id',place_id)