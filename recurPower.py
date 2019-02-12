#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Nov 15 08:34:24 2018

@author: makoto
"""

def recurPower(base, exp):
    '''
    @param base: int or float
    @param exp: whole number(int)
    @return int or float
    '''
    if exp == 0:
        return 1
    else:
        return base * recurPower(base, exp - 1)