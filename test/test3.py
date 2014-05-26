#!/usr/bin/env python
#-*- coding:utf-8 -*-
'''
#=============================================================================
#     FileName: test3.py
#         Desc: <F4>
#       Author: xiaolei ma
#        Email: koy1619@gmail.com
#     HomePage: http://www.linux48.com
#      Version: 0.0.1
#   LastChange: 2014-05-25 22:52:24
#      History:
#=============================================================================
'''

running = True
while running:

	money=raw_input('输入一个浮点数:')

#	Status=isinstance(money,float)
#	if Status==True and money < 1:
#		running = False
#	elif Status==False:
#		print '你输入的不是一个浮点数'
#		continue


#	if type(money)==type(0.0):
#		running = False
#	else:
#		print '你输入的不是一个浮点数'
#		continue

	if  float(money) < 1 and float(money) > 0:
		running = False

	else :
		print '您输入的不是一个浮点数'
		continue

	print money,'兑换结果是：'


	money = float(money)
	money = money*100
	money = int(money)  

	cent25=money/25
	money=money%25

	cent10=money/10
	money=money%10

	cent5=money/5
	money=money%5

	cent1=money

	if cent25:
	    print '25*',cent25
	if cent10:
	    print '10*',cent10
	if cent5:
	    print '5*',cent5
	if cent1:
	    print '1*',cent1
