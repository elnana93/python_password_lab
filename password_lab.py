#for loop
#lab 13 - projects lab

import random

capital_let = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
small_let = "abcdefghijklmnopqrstuvwxyz"
numbers = "0123456789"
special_char = "!@#$%^&*()_+?/\.,<>`~+=-{}[]|"

upper,lower,digits,odd = False,False,True,True

password = ""


if upper:
    password += capital_let
if lower:
    password += small_let
if digits:
    password += numbers
if odd:
    password += special_char

length = 20
howmuch = 10

for x in range(howmuch):
    password = "".join(random.sample(password,length))
    print(password) 
