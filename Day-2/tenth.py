import re
text = input("Enter the string:-\n")
regex = re.compile(r'^\d+$')
mo = regex.search(text)
print("You have entered the right string which start's with numeric digit and end with numeric digit  " + mo.group())
