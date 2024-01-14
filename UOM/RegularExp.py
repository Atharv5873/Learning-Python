import re
x='My  2 fav numbers for 69 and 420'
y=re.findall('\S+[aeiou]+\S',x)
print(y)