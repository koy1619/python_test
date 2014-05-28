#!/usr/bin/python
# coding = utf-8

'''
#=============================================================================
#     FileName: httplib_test.py
#         Desc: <F4>
#       Author: xiaolei.ma
#        Email: koy1619@gmail.com
#     HomePage: http://www.linux48.com
#      Version: 0.0.1
#   LastChange: 2014-05-28 11:12:57
#      History:
#=============================================================================
'''


def use_httplib():
	import httplib
	conn = httplib.HTTPConnection("linux48.com")
	i_headers = {"User-Agent": "Mozilla/5.0 (Windows; U; Windows NT 6.2; zh-CN; rv:1.9.1) Gecko/20090624 Firefox/3.5", "Accept": "text/plain"}
	conn.request("GET", "/", headers = i_headers)
	r1 = conn.getresponse()
	print "version:", r1.version
	print "reason:", r1.reason
	print "status:",r1.status
	print "msg:", r1.msg
	print "headers:", r1.getheaders()
	data = r1.read()
	print len(data)
	conn.close()

if __name__ == "__main__":
	use_httplib()