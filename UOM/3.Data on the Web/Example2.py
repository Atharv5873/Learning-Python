import xml.etree.ElementTree as ET
input='''<data>
    <users>
        <user x="2">
            <id>001</id>
            <name>Atharv</name>
        </user>
        <user x="7">
            <id>008</id>
            <name>Freya</name>
        </user>
    </users>
</data>'''

data=ET.fromstring(input)
lst=data.findall('users/user')
print('Number of users : ',len(lst))
for item in lst:
    print('\nName : ',item.find('name').text)
    print('ID : ',item.find("id").text)
    print("Attribute : ",item.get("x"))