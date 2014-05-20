#! /usr/bin/env python
# coding=utf-8
# Filename : if.py

'''
Created on 2014-5-20
@author: xiaolei.ma
'''

####continue语句####

while True:
    s = raw_input('随便写 : ')
    if s == 'quit':
        break
    if len(s) < 3:
        continue
    print '输入具有足够的长度'

