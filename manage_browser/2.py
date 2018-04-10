#encoding=utf8
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
	last="XMFM92232394549581755"
	T=True
	url = 'https://m.weibo.cn/status/GaS711TdY?mblogid=GaS711TdY&luicode=10000011&lfid=1076031771925961'
	times=1
	while (T and times<50):
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
			return now
	return "NULL"

if __name__ == '__main__':
	print time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
	print getWeb()
