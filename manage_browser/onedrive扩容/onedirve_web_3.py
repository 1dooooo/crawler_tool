# -*- coding:utf-8 -*-
from splinter import Browser
import time
import random
import string
import ixin
from splinter.exceptions import ElementDoesNotExist

User_Agent = 'Mozilla/5.0 (Windows NT 6.3; WOW64; rv:43.0) Gecko/20100101 Firefox/43.0'
header = {}
header['User-Agent'] = User_Agent
go_browser = Browser('chrome', user_agent='Mozilla/5.0 (iPhone; U; CPU like Mac OS X; en)')


def register(browser,url):
    username = getstr()
    print 'username=' + username+"@outlook.com"
    password="onedrive0.0"
    #password = getstr()
    print "password=" + password
    ming = getXM()
    print "ming=" + ming
    xing = getXM()
    print "xing=" + xing
    urlOnedrive = "https://onedrive.live.com?invref=28c11f63e1f77715&invscr=90"
    browser.visit(urlOnedrive)
    time.sleep(5000)
    browser.fill('MemberName', str(username))
    browser.find_by_id('iSignupAction').first.click()
    time.sleep(5)
    browser.fill('Password', str(password))
    browser.find_by_id('iSignupAction').first.click()
    time.sleep(2)
    browser.fill('LastName', str(username))
    browser.fill('FirstName', str(username))
    browser.find_by_id('iSignupAction').first.click()
    time.sleep(2)
    browser.find_by_xpath('//select[@id="BirthYear"]/option[@value="1996"]')._element.click()
    browser.find_by_xpath('//select[@id="BirthMonth"]/option[@value="6"]')._element.click()
    browser.find_by_xpath('//select[@id="BirthDay"]/option[@value="23"]')._element.click()
    browser.find_by_id('iSignupAction').first.click()
    time.sleep(2)
    phone = ixin.getPhone()
    if phone == 0:
        return 0
    time.sleep(6)
    try:
        browser.find_by_xpath('//input[starts-with(@id,"wlspispHIPPhone")]').first.fill(phone)
    except ElementDoesNotExist:
        print "打开网页超时，退出本次注册！"
        ixin.releasePhone(phone)
        return 0
    browser.find_by_xpath('//a[starts-with(@id,"wlspispHipSendCode")]').first.click()
    time.sleep(3)
    try:
        browser.find_by_xpath('//div[starts-with(@style,"text-align: left; display: inline;")]').first
    except ElementDoesNotExist:
        message = ixin.getMessage(phone)
        if message == 0:
            print "获得验证码超时，退出本次注册！"
            return 0
        browser.find_by_xpath('//input[starts-with(@id,"wlspispSolutionElement")]').first.fill(message)
        time.sleep(2)
        browser.find_by_id('iSignupAction').first.click()
        time.sleep(30)
        return 1
    else:
        print "手机号码不适用，退出本次注册！"
        time.sleep(2)
        ixin.releasePhone(phone)
        return 0
    return 0


def getstr():
    ran_str = "k" + ''.join(random.sample(string.ascii_letters + string.digits, 8))
    return ran_str


def getXM():
    ran_str = ''.join(random.sample(string.ascii_letters, 5))
    return ran_str

urlShort="https://signup.live.com/signup?wa=wsignin1.0&rpsnv=13&ct=1525010476&rver=6.7.6640.0&wp=MBI_SSL&wreply=https%3a%2f%2foutlook.live.com%2fowa%2f%3fnlp%3d1%26RpsCsrfState%3de25293fb-a756-48fd-89fd-804d2bc1edaf&id=292841&CBCXT=out&lw=1&fl=dob%2cflname%2cwld&cobrandid=90015&contextid=55A395BC680E1166&bk=1525010477&uiflavor=web&uaid=6d1d68269a13447181e6d59005867b26&mkt=ZH-CN&lc=2052&lic=1"
urlRegister = "https://signup.live.com/signup?wa=wsignin1.0&rpsnv=13&ct=1524322850&rver=6.7.6640.0&wp=MBI_SSL&wreply=https%3a%2f%2foutlook.live.com%2fowa%2f%3fnlp%3d1%26RpsCsrfState%3dfe8fb776-8654-24bd-4f0b-5dc4f84b4900&id=292841&CBCXT=out&lw=1&fl=dob%2cflname%2cwld&cobrandid=90015&contextid=93903750388BFD1B&bk=1524323087&uiflavor=web&uaid=7f30ff2d670a45b2a9167295e59a9d1e&mkt=ZH-CN&lc=2052&lic=1"
#ixin.login()
ok=1
while ok<=1:
    times = 0
    status = 0
    while status == 0:
        times += 1
        print "try for "+str(times)+"----"
        if ok==1:
            status = register(go_browser,urlRegister)
        else:
            status = register(go_browser,urlShort)
    print "success for "+str(ok)+"---------------------------------------------------"
    ok+=1
go_browser.quit()
exit(0)
