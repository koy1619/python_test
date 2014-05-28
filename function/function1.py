#! /usr/bin/env python
# coding=utf-8
# Filename: function1.py

'''
Created on 2014-5-20
@author: xiaolei.ma
'''

def sayHello():
    print 'Hello World!' # 属于该功能块

sayHello() # 调用函数

#函数作业计算闰年
#1
def isLeap(year) :  
    year = int(year)  
    if (year % 4 == 0 and year % 100 != 0) or year % 400 == 0 :  
        return True  
    else :  
        return False  
print isLeap(2000)

#2
def is_leap_year(year):
    if year % 100 == 0:
        return year % 400 == 0
    else:
        return year % 4 == 0
print is_leap_year(2012)

#3
import time

#计算今年是否是闰年，判断闰年条件，满足年份模400为0，或者模4为0但是模100不为0

thisyear = time.localtime()[0] #获取年份

if thisyear%400==0 or thisyear%4==0 and thisyear%100<>0:
    print '这是闰年'
else:
    print '不是闰年'

print thisyear

#4 while 循环

running = True
while running:

    def function(year):
        if (year % 4 == 0 and year % 100 !=0) or year %400 == 0 :
            return True
        else :
            return False

    year = int(raw_input("请输入年份:"))

    if function(year):
        print year,'是闰年'
        running = False
    else :
        print year,'不是闰年'


#判断
i = 1
x = 1
if i < 0:
    x = x+1
print x


print 5==6
print 5==5
print 5==6 and 3>=3
print 5==6 or 3>=3

#http://blog.csdn.net/killua_hzl/article/details/5607387
