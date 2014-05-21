#!/usr/bin/python
# coding=utf-8
'''
#=============================================================================
#     FileName: using_sys.py
#         Desc: <F4>
#       Author: xiaolei.ma
#        Email: koy1619@gmail.com
#     HomePage: http://www.linux48.com
#      Version: 0.0.1
#   LastChange: 2014-05-21 10:55:45
#      History:
#=============================================================================
'''

import sys

print 'The command line arguments are:'
for i in sys.argv:
    print i

print '\n\nThe PYTHON PATH is', sys.path, '\n' 
