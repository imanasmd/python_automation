import re
phoneNum = input("Enter the string:-\n")
regex = re.compile(r'(\d\d\d-)?\d\d\d-\d\d\d\d')
mo = regex.search(phoneNum)
print(mo.group())
