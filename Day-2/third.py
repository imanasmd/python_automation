import re
phoneNum = input("Enter the Phone number:-\n")
phoneRex = re.compile(r'(\d\d\d)\-(\d\d\d)\-(\d\d\d\d)')
mo = phoneRex.search(phoneNum)
print("Your complete mobile number " + mo.group())
print("First part mobile number " + mo.group(1))
print("second part mobile number " + mo.group(2))
print("Third part mobile number " + mo.group(3))

