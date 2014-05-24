#! /usr/bin/env python
# coding=utf-8
# Filename: func_default.py

'''
Created on 2014-5-20
@author: xiaolei.ma
'''

####默认参数值####

def say(message, times = 2):
	print message * times

say('你好 ')
say('Hello ',4)
say('World ',5)
