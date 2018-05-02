# -*- coding:utf-8 -*-
from user import *   #用户信息文件
from splinter import Browser
import urllib2
import lxml.html
import re
import pyperclip
import time

User_Agent = 'Mozilla/5.0 (Windows NT 6.3; WOW64; rv:43.0) Gecko/20100101 Firefox/43.0'
header = {}
header['User-Agent'] = User_Agent

def getWeb():
	pyperclip.copy("")
	urlLogin="https://account.xiaomi.com/pass/serviceLogin?callback=https%3A%2F%2Forder.mi.com%2Flogin%2Fcallback%3Ffollowup%3Dhttps%253A%252F%252Forder.mi.com%252Fqueue%252Ff2code%26sign%3DZDhhMGM4ZDlkNWQ2NmMyOGUzZDlhZTIwOGE5Y2EzYWJlMzZmOGY1ZQ%2C%2C&sid=mi_eshop&_bannerBiz=mistore&_qrsize=180"
	url = "https://order.mi.com/queue/f2code"
	browser = Browser('chrome', user_agent = 'Mozilla/5.0 (iPhone; U; CPU like Mac OS X; en)')
	browser.visit(urlLogin)
	browser.fill('user', str(username))
	browser.fill('password',str(password))
	browser.find_by_id('login-button').first.click()
	last="XMFM66795906258953955"
	T=True
	url = 'https://m.weibo.cn/status/GaS711TdY?mblogid=GaS711TdY&luicode=10000011&lfid=1076031771925961'
	times=1
	while (T and times<100):
		req = urllib2.Request(url,headers=header)
		res = urllib2.urlopen(req).read()
		code = re.findall(r"小爱音箱mini：(.+?)。",res)#
		now=code[0]
		if(last==now):
			print time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
			time.sleep(0.5)
			times+=1
		else:
			pyperclip.copy(now)
			browser.fill('fcode-input', str(now))
			#browser.fill('xm', xm.decode('utf-8'))
			browser.find_by_id('J_fcodeSubmit').first.click()
			#browser.wait_time(100)
			time.sleep(20)
			return now
	return "NULL"


print getWeb()


# url = "https://order.mi.com/queue/f2code"
# browser = Browser('chrome', user_agent = 'Mozilla/5.0 (iPhone; U; CPU like Mac OS X; en)')


# for i in range(0, 1):
#     if check(i):
#         break
#     time.sleep(1)
