#! /usr/bin/env python
# coding=utf-8

'''
#=============================================================================
#     FileName: test.py
#         Desc: <F4>
#       Author: xiaolei.ma
#        Email: koy1619@gmail.com
#     HomePage: http://www.linux48.com
#      Version: 0.0.1
#   LastChange: 2014-05-21 11:45:07
#      History:
#=============================================================================
'''


class A:
    def a(self):
        pass


class A1(A):
    def a1(self):
        pass


if __name__ == '__main__':
    print("dir without arguments:", dir())
    print("dir class A:", dir(A))
    print("dir class A1:", dir(A1))
    a = A1()
    print("dir object a(A1):", dir(a))
    print("dir function a.a:", dir(a.a))
