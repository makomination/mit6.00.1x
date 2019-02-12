#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Oct 18 23:56:17 2018

@author: makoto
"""

x = 7
ans = 0
itersLeft = x
while(itersLeft != 0):
    ans += x
    itersLeft -= 1
print(str(x) + '*' + str(x) + ' = ' + str(ans))