#! /usr/bin/env python
# coding=utf-8
# Filename : while.py

'''
Created on 2014-5-20
@author: xiaolei.ma
'''

####while语句####

running = True
number = 23

while running:
    guess = int(raw_input('输入一个数字 : '))

    if guess == number:
        print '恭喜你，你猜对了.' 
	running = False  # 回答正确将导致while循环停止
    elif guess < number:
        print '不对，比这个数字还大' 
    else:
        print '不对，比这个数字还小' 
else:
    print '这个while循环结束' 

print 'Done' 

