import re
text = input("Enter the text:-\n")
regex = re.compile(r'Iron(wo)*man')
mo = regex.search(text)
print("The action scene of " + mo.group())
