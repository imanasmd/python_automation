import re
text = input("Enter the string:-\n")
reg = re.compile(r'\@\#\$')
mo = reg.search(text)
print("your entered these characters:- " + mo.group())
