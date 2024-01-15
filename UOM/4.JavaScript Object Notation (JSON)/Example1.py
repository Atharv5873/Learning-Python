import json
data='''{
    "name":"Atharv",
    "Phone":{
    "type":"intl",
    "number":"8278800754"
    },
    "email":{"hide":"yes"}
    }'''
info=json.loads(data)
print("Name:",info["name"])
print("Phone:",info["Phone"]["number"])
print("Hide:",info["email"]["hide"])