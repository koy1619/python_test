#! /usr/bin/env python
# coding=utf-8

'''
#=============================================================================
#     FileName: using_list.py
#         Desc: <F4>
#       Author: xiaolei.ma
#        Email: koy1619@gmail.com
#     HomePage: http://www.linux48.com
#      Version: 0.0.1
#   LastChange: 2014-05-21 11:57:46
#      History:
#=============================================================================
'''

#这是我的购物列表
shoplist = ['apple','mango','pear','banana']

print '我有', len(shoplist),'种水果需要买.'

print '这些水果分别是:', #请注意逗号在行尾
for item in shoplist:
	print item,

print '\n我还需要买橘子哦.'
shoplist.append('orange') #使用append方法在列表中添加了一个项目
#append() 方法向列表的尾部添加一个新的元素。只接受一个参数,举例mylist.append('haha')
#extend()方法只接受一个列表作为参数，并将该参数的每个元素都添加到原有的列表中，举例mylist.extend(['123123','lalalala'])
print '我现在要买的水果是', shoplist

print '整理一下我的购买清单'
shoplist.sort() #使用列表的sort方法来对列表排序
print '购物清单排序', shoplist

print '我第一个要买的水果是', shoplist[0]
olditem = shoplist[0] #记住，Python从0开始计数,这里代表apple
del shoplist[0] #使用del语句删除apple
print '我已经买了', olditem
print '我现在还要买的水果是', shoplist
