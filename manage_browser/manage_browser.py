# -*- coding:utf-8 -*-
from splinter import Browser
import time


def check():
    browser.visit(url)
    browser.fill('fcode-input', str(fcode))
    #browser.fill('xm', xm.decode('utf-8'))
    browser.find_by_id('J_fcodeSubmit').first.click()
    if len(browser.find_by_tag('table')) == 1:
        return False
    else:
        return True


fcode = 410011172200000
url = "https://order.mi.com/queue/f2code"
browser = Browser('chrome', user_agent = 'Mozilla/5.0 (iPhone; U; CPU like Mac OS X; en)')
check()

# for i in range(0, 1):
#     if check(i):
#         break
#     time.sleep(1)
