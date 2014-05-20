#! /usr/bin/env python
# coding=utf-8
# Filename : if.py

'''
Created on 2014-5-20
@author: xiaolei.ma
'''

####if语句####

number = 25
guess = int(raw_input('请输入一个数字 : '))

if guess == number:
    print '恭喜你，你猜对了.'
    print "(但是你木有获得任何奖品!)" 
elif guess < number:
    print '不对，比这个数字还大'

#elif guess > number:
#    print '不对，比这个数字还小哦'

else:
    print '不对，比这个数字还小' 

print 'Done'
