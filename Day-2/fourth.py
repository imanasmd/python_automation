import re
ipadd = input("Enter the IP address:-\n")
ipaddrex = re.compile(r'\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}')
mo = ipaddrex.findall(ipadd)
print("Number of ip address are:- " + str(len(mo)))
print(mo)
