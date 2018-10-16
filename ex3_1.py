# -*- coding: utf-8 -*-
"""
Created on Sat Oct 13 10:38:39 2018

@author: michi
"""

integer = int(input("Enter an integer: "))

root = 0
end = False
while root < integer:
    pwr = 1
    while pwr < 6:
        if root**pwr == integer:
            print(root, pwr)
            end = True
            break
        pwr += 1
    root += 1

if not end:
    print("No such pair exists")