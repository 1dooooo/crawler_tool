
#encoding=utf8
import urllib2
import lxml.html
import csv

User_Agent = 'Mozilla/5.0 (Windows NT 6.3; WOW64; rv:43.0) Gecko/20100101 Firefox/43.0'
header = {}
header['User-Agent'] = User_Agent

'''
获取所有代理IP地址
'''
def getWeb():
    web = []
    for i in range(1,101):
        try:
            url = 'http://www.alexa.cn/siterank/'+str(i)
            req = urllib2.Request(url,headers=header)
            res = urllib2.urlopen(req).read()
            tree=lxml.html.fromstring(res)
            ok=tree.cssselect('ul.siterank-sitelist > li > div.info-wrap > div.domain')
            for x in range(0,len(ok)):
                div = ok[x]
                domain = div[0].text_content()
                web.append(domain)
        except:
            continue
    return web

if __name__ == '__main__':
    writer = csv.writer(open('web_top.csv', 'wb'))
    writer.writerow(['rank','domain'])
    web_all=getWeb()
    for x in range(0,len(web_all)):
        row=(x,web_all[x])
        writer.writerow(row)