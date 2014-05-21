#! /usr/bin/env python
# coding=utf-8

'''
#=============================================================================
#     FileName: using_dict.py
#         Desc: <F4>
#       Author: xiaolei.ma
#        Email: koy1619@gmail.com
#     HomePage: http://www.linux48.com
#      Version: 0.0.1
#   LastChange: 2014-05-21 14:20:10
#      History:
#=============================================================================
'''

# 'ab' is short for 'a'ddress'b'ook

ab = {       'Swaroop'   : 'swaroopch@byteofpython.info',
             'Larry'     : 'larry@wall.org',
             'Matsumoto' : 'matz@ruby-lang.org',
             'Spammer'   : 'spammer@hotmail.com'
     }

print "Swaroop 的地址为 %s" % ab['Swaroop']
print "Spammer 的地址为 %s" % ab['Spammer']

print '\n在旧地址簿里面有以下 %d 个联系人:\n' % len(ab)
for name, address in ab.items():
    print '联系 %s 的地址是 %s' % (name, address)

print '\n在地址簿添加一个联系人Guido'
ab['Guido'] = 'guido@python.org'

print '在地址簿删除一个联系人Spammer'
del ab['Spammer']

print '\n在新地址簿里面有以下 %d 个联系人:\n' % len(ab)
for name, address in ab.items():
    print '联系 %s 的地址是 %s' % (name, address)

if 'Guido' in ab: # OR ab.has_key('Guido')
    print "\nGuido 的地址为 %s" % ab['Guido'] 

if 'Spammer' in ab: # OR ab.has_key('Spammer')
    print "\nSpammer 的地址为 %s" % ab['Spammer']
