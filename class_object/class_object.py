#! /usr/bin/env python
# coding=utf-8

'''
#=============================================================================
#     FileName: class_object.py
#         Desc: <F4>
#       Author: xiaolei ma
#        Email: koy1619@gmail.com
#     HomePage: http://www.linux48.com
#      Version: 0.0.1
#   LastChange: 2014-05-24 17:37:13
#      History:
#=============================================================================
'''
class Bird(object):
    have_feather = True
    way_of_reproduction  = 'egg'
    def move(self,dx,dy):
        position = [0,0]
        position[0] = position[0] + dx
        position[1] = position[1] + dy
        return position

class Chicken(Bird):
    way_of_move = 'walk'
    position_in_KFC = True

class Oriole(Bird):
    way_of_move = 'fly'
    position_in_KFC = False

summer3 = Chicken()
summer1 = Bird()
summer2 = Bird()

print summer1.way_of_reproduction
print summer1.have_feather
print summer2.have_feather
print summer3.have_feather
print 'summer1开始移动到坐标:',summer1.move(5,8)
print 'summer2开始移动到坐标:',summer2.move(6,9)
print 'summer3开始移动到坐标:',summer3.move(5,7)
