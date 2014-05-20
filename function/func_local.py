#! /usr/bin/env python
# coding=utf-8
# Filename: func_local.py

'''
Created on 2014-5-20
@author: xiaolei.ma
'''

####局部变量####

def func(x):
    print 'x值为', x
    x = 2
    print '更改本地x到', x

x = 50
func(x)
print 'x的值仍然是', x 

