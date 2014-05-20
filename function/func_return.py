#! /usr/bin/env python
# coding=utf-8
# Filename: func_return.py

'''
Created on 2014-5-20
@author: xiaolei.ma
'''

####return语句####

def maximum(x,y):

	if x > y:
		return x

	else:
		return y

#代入实参
print maximum(20, 30)


#代入形参
x = 50
y = 40
print  maximum(x, y)


