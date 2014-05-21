#! /usr/bin/env python
# coding=utf-8
'''
#=============================================================================
#     FileName: str_methods.py
#         Desc: 
#       Author: xiaolei.ma
#        Email: koy1619@gmail.com
#     HomePage: http://www.linux48.com
#      Version: 0.0.1
#   LastChange: 2014-05-21 16:51:14
#      History:
#=============================================================================
'''

name = 'Swaroop' # This is a string object 

if name.startswith('Swa'):  #startwith方法是用来测试字符串是否以给定字符串开始
    print 'Yes, the string starts with "Swa"'

if 'a' in name:  #in操作符用来检验一个给定字符串是否为另一个字符串的一部分
    print 'Yes, it contains the string "a"'

if name.find('war'):  #find方法用来找出给定字符串在另一个字符串中的位置
    print 'Yes, it contains the string "war"'

else:
    print 'No, can not find this words'

delimiter = '_*_'
mylist = ['Brazil', 'Russia', 'India', 'China']
print delimiter.join(mylist) 

