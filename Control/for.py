#! /usr/bin/env python
# coding=utf-8
# Filename : for.py

'''
Created on 2014-5-20
@author: xiaolei.ma
'''

####for循环####

for i in range(1,10):
    print i
else:
    print 'for循环结束' 


####九九乘法表####

for i in range(1,10):
    for j in range(1,i+1):
        m = j*i
        print '%d x %d = %d\t' %(j,i,m), 
    print '' 
