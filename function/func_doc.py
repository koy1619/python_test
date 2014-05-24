#! /usr/bin/env python
# coding=utf-8
# Filename: func_doc.py

'''
Created on 2014-5-20
@author: xiaolei.ma
'''

####DocStrings(文档字符串)####

def printMax(x, y):
    '''打印两个数中的最大值.

    这两个值必须是整数.'''
    x = int(x) #尽可能转换为整数
    y = int(y)

    if x > y:
        print x, '是最大值'
    else:
        print y, '是最大值'

#代入实参
printMax(3, 5)
print printMax.__doc__

##代入形参
x = 5
y = 7
printMax(x, y)
print printMax.__doc__
