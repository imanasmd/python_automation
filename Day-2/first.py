from re import *
phoneRex =  compile(r'\+\d\d\d\d\d\d\d\d\d\d\d\d')  # \d this shorthand character stands for single numeric character
mobileNum = input("Enter the mobile number:-\n")
mo = phoneRex.search(mobileNum)
print("Your mobile number is " + mo.group())

