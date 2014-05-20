#! /usr/bin/env python
# coding=utf-8
# Filename: func_param.py

'''
Created on 2014-5-20
@author: xiaolei.ma
'''

####函数形参####

def printMax(a, b):
    if a > b:
        print a, '是最大值'
    else:
        print b, '是最大值'

printMax(3, 4) # 直接给文字值(实参)

x = 5
y = 18
printMax(x, y) # 给变量作为参数(形参)

