#!/usr/bin/env python
#-*- coding:utf-8 -*-
#5-5 取余。取一个任意小于1 美元的金额，然后计算可以换成最少多少枚硬币。硬币有1
#美分，5 美分，10 美分，25 美分四种。1 美元等于100 美分。举例来说，0.76 美元换算结果
#应该是 3 枚25 美分，1 枚1 美分。类似76 枚1 美分，2 枚25 美分+2 枚10 美分+1 枚5 美分+1
#枚1 美分这样的结果都是不符合要求的。
money = raw_input('输入任意小于1 美元的金额:')
print money,'美元换算结果'
money = float(money)
money *= 100
money = int(money)
cent25 = money / 25
money %= 25
cent10 = money / 10
money %= 10
cent5 = money / 5
money %= 5
cent1 = money
if cent25 :
    print '25美分*',cent25
if cent10 :
    print '10美分*',cent10
if cent5 :
    print '5美分*',cent5
if cent1 :
    print '1美分*',cent1
