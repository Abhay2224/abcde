# Write a program for generating regular expressions for regular grammar

import re

mbno = input('Enter mobile number: ')
mob_valpat="[o|91]?[-\s]?[6-9]\d{9}"
if re.search(mob_valpat,mbno):
    print("Valid Mobile Number")
else:
    print("Not a Valid Mobile No")

#-----------------------------------------------------------#    

email_cond = "^[a-z]+[a-z 0-9]+[@]\w+[.]\w{2,3}$"
user_email=input("Enter your email ")
if re.search(email_cond,user_email):
    print("Right email")
else:
    print("Wrong Email")
