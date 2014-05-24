#! /usr/bin/env python
# coding=utf-8
# Filename: func_key.py

'''
Created on 2014-5-20
@author: xiaolei.ma
'''

####关键参数####

def func(a, b=5, c=10):
	print 'a is', a, 'and b is', b, 'and c is', c


func(3, 7)
func(25, c=24)
func(c=50, a=100)
