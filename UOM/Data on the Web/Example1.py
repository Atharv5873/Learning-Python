import xml.etree.ElementTree as ET
data='''<person>
    <name>Atharv</name>
    <phone type="intl">+91 82788 00754</phone>
    <email hide="yes"/>
    </person>'''

tree=ET.fromstring(data)
print('Name :',tree.find('name').text)
print("Number :",tree.find('phone').text)
print('Attr :',tree.find('email').get('hide'))
       