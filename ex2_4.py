# -*- coding: utf-8 -*-
"""
Created on Fri Oct 12 20:35:44 2018

@author: michi
"""
n = 10
largest_odd = None
while n > 0:
    integer = int(input("enter an integer: "))
    
    if not integer % 2 == 0:
        if largest_odd:
            if integer > largest_odd:
                largest_odd = integer
        else:
            largest_odd = integer
    n -= 1
print(largest_odd)