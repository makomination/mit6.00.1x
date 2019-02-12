#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Oct  6 23:28:23 2018

@author: makoto
"""

def babylonianAlgo(a):
    if(a <= 0):
        return 0;
    x1 = 1;
    xn  = (x1 + a/x1) / 2;
    xn1 = (xn + a/xn)/ 2;
    i = 0;
    while(xn != xn1):
        i+=1;
        xn = (xn1 + a/xn1) / 2;
        xn1 = (xn + a/xn) / 2;
        #print(xn1);
    print(i);
    return xn1;

#print(babylonianAlgo(14393));