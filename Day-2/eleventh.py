import re
text = input("Enter the text:-\n")
regex = re.compile(r'.at')
match = regex.findall(text)
print(match)

