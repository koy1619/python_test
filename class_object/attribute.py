#! /usr/bin/env python
# coding=utf-8

'''
#=============================================================================
#     FileName: attribute.py
#         Desc: <F4>
#       Author: xiaolei ma
#        Email: koy1619@gmail.com
#     HomePage: http://www.linux48.com
#      Version: 0.0.1
#   LastChange: 2014-05-24 19:34:40
#      History:
#=============================================================================
'''
class Human(object):
    """docstring for Human"""
    def __init__(self, input_gender):
        self.gender = input_gender

    def printGender(self):
        print self.gender

lilei = Human('male')
print lilei.gender
lilei.printGender()

print(0b1110)
