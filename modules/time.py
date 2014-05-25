#!/usr/bin/python
# coding=utf8
'''
#=============================================================================
#     FileName: time.py
#         Desc: <F4>
#       Author: xiaolei ma
#        Email: koy1619@gmail.com
#     HomePage: http://www.linux48.com
#      Version: 0.0.1
#   LastChange: 2014-05-25 18:28:40
#      History:
#=============================================================================
'''


import time
import datetime 

#计算今年是否是闰年，判断闰年条件，满足年份模400为0，或者模4为0但是模100不为0

thisyear = time.localtime()[0] #获取年份

if thisyear%400==0 or thisyear%4==0 and thisyear%100<>0:
    print '这是闰年'
else:
    print '不是闰年'

print thisyear

thisyear = time.localtime() #获取年份具体
print thisyear

if __name__ == '__main__':
#    time.sleep(1)
    print "clock1:%s" % time.clock()
#    time.sleep(1)
    print "clock2:%s" % time.clock()
 #   time.sleep(1)
    print "clock3:%s" % time.clock()

#两日期相减 
  
d1 = datetime.datetime(2005, 2, 16) 
d2 = datetime.datetime(2004, 12, 31) 
print (d1 - d2).days

#开始时间和结束时间
starttime = datetime.datetime.now() 
endtime = datetime.datetime.now() 

print datetime.datetime.now()

print (endtime - starttime).seconds
