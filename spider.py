#coding=utf-8

#------------------------
#
# Author: MonsterClown
#
# Data: 2015-09-08
#
#------------------------


import urllib
import urllib2
import re


#----配置-----------------------------------------------------------------------
reqMode = '0'   #0->常规请求， 1->Post请求， 2->Get请求
url = 'http://www.cuit.edu.cn'
datas ={'id' : '1644'}
User_Agent = 'Mozilla/5.0 (Windows NT 6.3; rv:36.0) Gecko/20100101 Firefox/40.0'

################################################################################


#----常规请求-------------------------------------------------------------------
def getHtml(url):

	try:
		response = urllib2.urlopen(url)
	
	except URLError, e:
		
		if hasattr(e, 'code'):
			print 'The Server couldn\'t fullfill the request.'
			print 'Error Code: ', e.code

		elif hasattr(e, 'reason'):
			print 'We failed to reach the Server.'
			print 'Reason: ', e.reason

	else:
		html = response.read()
		return html


#----Post请求-------------------------------------------------------------------
def getHtmlByPost(url, datas):
	
	postData = urllib.urlencode(datas)    #对数据进行编码
	req = urllib2.Request(url, postData)  #POST请求
	
	try:
		response = urllib2.urlopen(req)   #接收返回
	
	except URLError, e:

		if hasattr(e, 'code'):
			print 'The Server couldn\'t fullfill the request.'
			print 'Error Code: ', e.code
	
		elif hasattr(e, 'reason'):
			print 'We failed to reach the Server.'
			print 'Reason: ', e.reason

	else:
		html = response.read()				  #读取返回
		return html


#----Get请求--------------------------------------------------------------------
def getHtmlByGet(url, datas):
	
	url_values = urllib.urlencode(datas)  #编码数据
	full_url = url + '?' + url_values	  #拼接url
#	print full_url
	
	try:
		response = urllib2.urlopen(full_url)
	
	except URLError, e:

		if hasattr(e, 'code'):
			print 'The Server couldn\'t fullfill the request.'
			print 'Error Code: ', e.code
	
		elif hasattr(e, 'reason'):
			print 'We failed to reach the Server.'
			print 'Reason: ', e.reason
	
	else:	
		html = response.read()
		return html


#################################################################################


#----请求方式选择----------------------------------------------------------------

html = {
	'0': getHtml(url),					#常规请求
	'1': getHtmlByPost(url, datas),		#Post请求
	'2': getHtmlByGet(url, datas)		#Get请求
}[reqMode]

#################################################################################


print html

page = file('test.html', 'w')
page.write(html) 
