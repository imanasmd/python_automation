import re
text = input("Enter the string:-\n")
reg = re.compile(r'Ironman|Thor')
m1 = reg.search(text)
print("First occurence is " + m1.group())
