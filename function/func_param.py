#! /usr/bin/env python
# coding=utf-8
# Filename: function1.py

'''
Created on 2014-5-20
@author: xiaolei.ma
'''

def printMax(a, b):
    if a > b:
        print a, 'is maximum'
    else:
        print b, 'is maximum'

printMax(3, 4) # directly give literal values

x = 5
y = 7

printMax(x, y) # give variables as arguments 

