import re
x='My  2 fav numbers for 69 and 420'
a=re.findall('\S+[aeiou]+\S',x)
b=re.findall('[aeiou]',x)
c=re.findall('\S+[a-z]+\S',x)
d=re.findall('[0-9]+',x)
print('a=',a)
print('b=',b)
print('c=',c)
print('d=',d)