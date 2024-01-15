import json
data='''
    [{
        "id":"001",
        "x":"2",
        "name":"Atharv"
    },{
    "id":"002",
    "x":"7",
    "name":"Freya"
    }  
    ]
    '''
info=json.loads(data)
print('USer Count: ',len(info))
for i in info:
    print('\nName: ',i["name"])
    print('Id: ',i["id"])
    print('Attribute: ',i["x"])

