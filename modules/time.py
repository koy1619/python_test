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
'''
#运行时间： 
   

starttime = datetime.datetime.now() 
endtime = datetime.datetime.now() 
print (endtime - starttime).seconds
  
#计算当前时间向后10天的时间。 
# 如果是小时 days 换成 hours 
  
  
d1 = datetime.datetime.now() 
d3 = d1 datetime.timedelta(days =10) 
  
print str(d3) 
print d3.ctime()

time.ctime([sec])#把秒数转换成日期格式，如果不带参数，则显示当前的时间。
 
>>> import time
>>> time.ctime()
>>> "Wed Jun 14 15:02:50 2006"
>>> time.ctime(1138068452427683)
"Sat Dec 14 04:51:44 1901" 
>>> import time
>>> time.strftime("%Y-%m-%d %X",time.localtime())
"2011-03-15 20:42:12"
>>> time.strftime("%Y-%m-%d %H:%M:%S",time.localtime())
"2011-03-15 20:03:47"
DateTime模块
－－－－－－－－－－－－－－－－－－－－－－－－－－－－
datetime 将日期转化为秒
>>> import datetime,time
>>> time.mktime(datetime.datetime(2009,1,1).timetuple())
1230739200.0
>>> cc=[2000,11,3,12,43,33] #Attributes: year, month, day, hour, minute, second
>>> time.mktime(datetime.datetime(cc[0],cc[1],cc[2],cc[3],cc[4],cc[5]).timetuple())
973226613.0
time.time()取得当前时间；
time.localtime()取得本地时间；
time.strftime()格式化日期；
time.strptime(timeString)把字符串转化为日期；

判断输入的日期是星期几
>>> datetime.datetime(2011,02,15).weekday()
1
>>> datetime.datetime(2011,02,15).weekday()
1
>>> datetime.datetime(2011,02,16).weekday()
2
>>> datetime.datetime(2011,02,17).weekday()
3
>>>
datetime模块获取当前时间
>>> datetime.datetime.utcnow()
datetime.datetime(2011, 3, 15, 13, 19, 32, 264194)
>>> datetime.datetime.utcnow().strftime("%Y-%m-%d %H:%M:%S") 格式化
'2011-03-15 13:19:27'
>>>
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
