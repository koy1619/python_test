#! /usr/bin/env python
# coding=utf-8
# Filename : break.py

'''
Created on 2014-5-20
@author: xiaolei.ma
'''

####break语句####

while True:
    s = raw_input('随便写 : ')
    if s == 'quit':
        break
    print '字符串的长度是', len(s)
print 'Done' 

