#! /usr/bin/env python
# coding=utf-8
# Filename : test.py

'''
Created on 2014-5-20
@author: xiaolei.ma
'''

s = '''This is a multi-line string.
This is the second line.
This is the third line'''
print s

m = 'This is a string. \
This continues the string.'
print m

a=9;b=5
c=a|b
d=a&b
e=a^b
f=c|d|e
g=f*d
print c
print d
print e
print f
print g
print 'Area is', g
print 'Perimeter is',2*(f+d)*g
