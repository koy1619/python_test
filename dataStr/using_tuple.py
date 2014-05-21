#! /usr/bin/env python
# coding=utf-8

'''
#=============================================================================
#     FileName: using_tuple.py
#         Desc: <F4>
#       Author: xiaolei.ma
#        Email: koy1619@gmail.com
#     HomePage: http://www.linux48.com
#      Version: 0.0.1
#   LastChange: 2014-05-21 11:57:46
#      History:
#=============================================================================
'''

A_zoo = ('wolf', 'elephant', 'penguin')
print 'A动物园有', len(A_zoo),'种动物'

B_zoo = ('monkey', 'dolphin', A_zoo)
print 'B动物园有', len(B_zoo),'种动物'
print 'B动物园有这些动物', B_zoo
print '从A动物园带来的动物是', B_zoo[2]
print '最后从A动物园带来的动物是', B_zoo[2][2]
