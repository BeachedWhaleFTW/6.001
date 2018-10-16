# -*- coding: utf-8 -*-
"""
Created on Wed Oct 10 19:15:29 2018

@author: michi
"""

def largest_odd(x, y, z):
    largest = None
    x_odd = None
    y_odd = None
    z_odd = None
    
    if not x % 2 == 0:
        x_odd = True
    else:
        x_odd = False
    if not y % 2 == 0:
        y_odd = True
    else:
        y_odd = False
    if not z % 2 == 0:
        z_odd = True
    else:
        z_odd = False
    
    if x_odd and y_odd and z_odd:
        if x >= y and x >= z:
            largest = x
        elif y >= x and y >= z:
            largest = y
        elif z >= x and z >= y:
            largest = z
    elif x_odd and y_odd:
        if x >= y:
            largest = x
        else:
            largest = y
    elif x_odd and z_odd:
        if x >= z:
            largest = x
        else:
            largest = z
    elif y_odd and z_odd:
        if y >= z:
            largest = y
        else:
            largest = z
    elif x_odd:
        largest = x
    elif y_odd:
        largest = y
    elif z_odd:
        largest = z
    else:
        print("No numbers are odd")
    return largest

print(largest_odd(1, 1, 3))
print(largest_odd(2, 2, 2))
print(largest_odd(3, 1, 1))
print(largest_odd(5, 2, 4))