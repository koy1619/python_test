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

	money=raw_input('输入任意小于1 美元的金额:')
	print money,'美分兑换结果是：'

#	Status=isinstance(money,float)
#	if Status==True :
#		running = False
#	elif Status!=True:
#		print '你输入的不是一个浮点数'

	if '.' in str(money):
		running=False
	else:
		print '您输入的不是一个浮点数'
		continue


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
	    print '25美分*',cent25
	if cent10:
	    print '10美分*',cent10
	if cent5:
	    print '5美分*',cent5
	if cent1:
	    print '1美分*',cent1
