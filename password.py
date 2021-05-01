# -*- coding: utf-8 -*-

"password genrator"
import string
import random
import numpy as np
Ustrings=string.ascii_lowercase
Lstrings=string.ascii_uppercase
num = np.array([i for i in range(10)])
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']
length=int(input("enter the length of password: "))
UC=int(input("enter the number of uppercase letters required: "))
LC=int(input("enter the number of lowercase letters required: "))
syb=int(input("enter the number of symbols requried: "))
password=""
for char in range(1, UC + 1):
    password= password + random.choice(Ustrings)
for char in range(1, LC + 1):
    password= password + random.choice(Lstrings)
for char in range(1, syb + 1):
    password= password + random.choice(symbols)
print(password)
list1=list(password)
print(list1)
random.shuffle(list1)
print(list1)
finalPasswprd = ''.join(list1)
print("the genrator password: ",finalPassword)
