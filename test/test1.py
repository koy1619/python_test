#!/usr/bin/env python
#-*- coding: utf-8 -*-
'''
#=============================================================================
#     FileName: test1.py
#         Desc: <F4>
#       Author: xiaolei ma
#        Email: koy1619@gmail.com
#     HomePage: http://www.linux48.com
#      Version: 0.0.1
#   LastChange: 2014-05-25 18:58:29
#      History:
#=============================================================================
'''

#5-3 标准类型运算符. 写一段脚本，输入一个测验成绩，根据下面的标准，输出他的评分成绩（A-F）。
#A: 90–100 B: 80–89 C: 70–79 D: 60 F: <60

while True :
    fenshu = int(raw_input('请输入一个分数：'))

    if fenshu > 100 or fenshu < 0 :
        print '输入分数无效，程序退出'
        break

    elif fenshu >= 90 :
        print '%d is rank A' % fenshu

    elif fenshu >= 80 :
        print '%d is rank B' % fenshu

    elif fenshu >= 70 :
        print '%d is rank C' % fenshu

    elif fenshu >= 60 :
        print "%d is rank D" % fenshu

    else :
        print '%d is rank F' % fenshu
