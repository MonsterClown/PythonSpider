#coding=utf-8

#------------------------
#
# Author: MonsterClown
#
# Data: 2015-09-10
#
#------------------------


import urllib
import urllib2
import re


#----配置-----------------------------------------------------------------------
reqMode = 0  #0->常规请求， 1->Post请求， 2->Get请求
url = 'http://blog.csdn.net/pleasecallmewhy/article/details/8923067'
datas ={'id' : '1644'#，
#		'name' : '123'
}
headers = {
	'User-Agent' : 'User-Agent: Mozilla/5.0 (X11; Linux x86_64; rv:40.0) Gecko/20100101 Firefox/40.0',
#	'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
#	'Accept-Charset' : 'utf-8,ISO-8859-1',
#	'Accept-Encoding':'gzip,deflate',
	'Connection':'keep-alive',
	'Referer':None 
}
################################################################################


#----常规请求-------------------------------------------------------------------
def getHtml(url):
	print '请求方式： 常规请求'
	print '请求URL：' + url	

	try:
		req = urllib2.Request(url, None, headers)
		response = urllib2.urlopen(req)
	
	except urllib2.URLError, e:
		if hasattr(e, 'code'):
			print 'HTTPError：服务器无法完成请求。'
			print '错误代码：', e.code
			exit()
	
		elif hasattr(e, 'reason'):
			print 'URLError：未能到达服务器。'
			print '原因： ', e.reason
			exit()
	
	else:
		print '真实URL：' + response.geturl()
		print 'Http信息：'
		print response.info()
		html = response.read()
		return html

#----Post请求-------------------------------------------------------------------
def getHtmlByPost(url, datas):	
	print '请求方式： Post请求'
	print '请求URL：' + url
	postData = urllib.urlencode(datas)    #对数据进行编码
	print 'Post内容：' + postData
	req = urllib2.Request(url, postData, headers)  #POST请求

	try:
		response = urllib2.urlopen(req)   #接收返回
	
	except urllib2.URLError, e:
		if hasattr(e, 'code'):
			print 'HTTPError：服务器无法完成请求。'
			print '错误代码：', e.code
			exit()
		
		elif hasattr(e, 'reason'):
			print 'URLError：未能到达服务器。'
			print '原因： ', e.reason
			exit()
	
	else:
		print '真实URL：' + response.geturl()
		print 'Http信息：'
		print response.info()
		html = response.read()
		return html

#----Get请求--------------------------------------------------------------------
def getHtmlByGet(url, datas):
	print '请求方式：Get请求'
	print '请求URL：' + url
	url_values = urllib.urlencode(datas)  #编码数据
	full_url = url + '?' + url_values	  #拼接url
	print '完整URL：' + full_url
	
	try:
		req = urllib2.Request(full_url, None, headers)
		response = urllib2.urlopen(req)
	
	except urllib2.URLError, e:
		if hasattr(e, 'code'):
			print 'HTTPError：服务器无法完成请求。'
			print '错误代码：', e.code
			exit()
	
		elif hasattr(e, 'reason'):
			print 'URLError：未能到达服务器。'
			print '原因： ', e.reason
			exit()
	
	else:	
		print '真实URL：' + response.geturl()
		print 'Http信息：'
		print response.info()
		html = response.read()
		return html

#################################################################################


#----请求方式选择----------------------------------------------------------------
if reqMode == 0:
	html = getHtml(url)

elif reqMode == 1:
	html = getHtmlByPost(url, datas)

elif reqMode == 2:
	html = getHtmlByGet(url, datas)

#################################################################################


#print html

page = file('test.html', 'w')
page.write(html) 
