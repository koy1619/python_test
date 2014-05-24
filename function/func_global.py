#! /usr/bin/env python
# coding=utf-8
# Filename: func_global.py

'''
Created on 2014-5-20
@author: xiaolei.ma
'''

def func():
    global x

    print 'x的值为', x
    x = 2
    print '修改本地x值为', x

x = 50
func()
print 'x的值为', x 
