from re import *
mobileNum = input("Enter the mobile number:-\n")
mo = search(r'\+\d\d\d\d\d\d\d\d\d\d\d\d',mobileNum)
print("Your mobile number is " + mo.group())

