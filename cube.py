#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Oct 19 12:00:48 2018

@author: makoto
"""

x = int(input('Enter an integer: '))
ans = 0
while ans**3 < abs(x):
    ans += 1
if ans**3 != abs(x):
    print(str(x) + ' is not a perfect cube')
else:
    if x < 0:
        ans = -ans
    print('Cube root of ' + str(x) + ' is ' + str(ans))