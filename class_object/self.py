#! /usr/bin/env python
# coding=utf-8

'''
#=============================================================================
#     FileName: self.py
#         Desc: <F4>
#       Author: xiaolei ma
#        Email: koy1619@gmail.com
#     HomePage: http://www.linux48.com
#      Version: 0.0.1
#   LastChange: 2014-05-24 18:02:16
#      History:
#=============================================================================
'''

class Human(object):
    laugh = '哈哈'
    def show_laugh(self):
        print self.laugh

    def laugh_2th(self):
        for i in range(2):
            self.show_laugh()

    def laugh_5th(self):
        for i in range(5):
            self.show_laugh()

print 'li_lei laugh'
li_lei = Human()          
li_lei.laugh_5th()

print 'li_lei2 laugh'
li_lei2 = Human()
li_lei2.laugh_2th()
