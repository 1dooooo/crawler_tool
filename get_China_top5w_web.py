#encoding=utf8
import urllib2
import lxml.html
import csv

User_Agent = 'Mozilla/5.0 (Windows NT 6.3; WOW64; rv:43.0) Gecko/20100101 Firefox/43.0'
header = {}
header['User-Agent'] = User_Agent

def getWeb():
    web = []
    for i in range(1,2):
        try:
            print i
            url = 'http://top.chinaz.com/all/index_'+str(i)+'.html'
            if i== 1:
                url = 'http://top.chinaz.com/all/index.html'
            req = urllib2.Request(url,headers=header)
            res = urllib2.urlopen(req).read()
            tree=lxml.html.fromstring(res)
            step_1=tree.cssselect('div.TopListCent-listWrap > ul.listCentent > li')
            for x in range(0,len(step_1)):
                step_2 = step_1[x]
                ok = step_2.cssselect('div.CentTxt > h3.rightTxtHead > span.col-gray')
                domain = ok[0].text_content()
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
    print web_all