import re
file = open('D:\\Coding\\Python\\Learning-Python\\UOM\\Regular Expressions\\Assignment\\Actual.txt')
Sum = 0
for line in file:
    line = line.rstrip()
    numbers = re.findall('[0-9]+', line)
                 
print(Sum)
