#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Nov 12 13:01:24 2018

@author: makoto
"""

epsilon = 0.0001
y = 24.0
guess = y/2.0
numGuesses = 0

while abs(guess * guess - y) >= epsilon:
    numGuesses += 1
    guess = guess - (((guess ** 2) - y) / (2 * guess))
print('numGuesses = ' + str(numGuesses))
print('Square root of ' + str(y) + ' is about ' + str(guess))
