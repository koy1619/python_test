#! /usr/bin/env python
# coding=utf-8

'''
#=============================================================================
#     FileName: seq.py
#         Desc: <F4>
#       Author: xiaolei.ma
#        Email: koy1619@gmail.com
#     HomePage: http://www.linux48.com
#      Version: 0.0.1
#   LastChange: 2014-05-21 15:05:00
#      History:
#=============================================================================
'''

shoplist = ['apple', 'mango', 'carrot', 'banana']

print 'Item start to end is', shoplist[:]
# Indexing or 'Subscription' operation
print 'Item 0 is', shoplist[0]
print 'Item 1 is', shoplist[1]
print 'Item 2 is', shoplist[2]
print 'Item 3 is', shoplist[3]
print 'Item -1 is', shoplist[-1]
print 'Item -2 is', shoplist[-2]

# Slicing on a list
print 'Item 1 to 3 is', shoplist[1:3]
print 'Item 2 to end is', shoplist[2:]
print 'Item 1 to -1 is', shoplist[1:-1]

# Slicing on a string
name = 'swaroop'
print '\ncharacters start to end is', name[:]
print 'characters 1 to 3 is', name[1:3]
print 'characters 2 to end is', name[2:]
print 'characters 1 to -1 is', name[1:-1]
