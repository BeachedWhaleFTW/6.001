# -*- coding: utf-8 -*-
"""
Created on Fri Oct 12 20:50:38 2018

@author: michi
"""

def string_sum(s):
    total = 0
    for c in s:
        if c.isdigit():
            total += int(c)
    return total

print(string_sum('1.23,2.4,3.123'))
print(string_sum('days'))
print(string_sum('dalkjhi3lkjad'))