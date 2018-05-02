# coding=utf-8
import urllib2
import re
import time

username = ""
password = ""
token = ""


def login():
    response = urllib2.urlopen(
        "http://api.ixinsms.com/api/do.php?action=loginIn&name=" + username + "&password=" + password)
    html = response.read()
    result = html.split('|')
    if result[0] == '1':
        return result[1]
    else:
        print "login error"


def getPhone():
    response = urllib2.urlopen(
        "http://api.ixinsms.com/api/do.php?action=getPhone&sid=1257" + "&token=" + token)
    html = response.read()
    result = html.split('|')
    if result[0] == '1':
        print "[1]get phone number:" + result[1]
        return result[1]
    else:
        print "[1]get phone number error"
    return 0


def getMessage(phone):
    i = 1
    while i < 21:
        response = urllib2.urlopen(
            "http://api.ixinsms.com/api/do.php?action=getMessage&sid=1257" + "&phone=" + phone + "&token=" + token)
        html = response.read()
        result = html.split('|')
        if result[0] == '1':
            messageCode = re.findall(r"访问代码: (.+?)【PIN】", result[1])
            print "[2]get phone message:" + messageCode[0]
            return messageCode[0]
        else:
            print "[2]get phone message error at " + str(i) + " times ,stop for 5s .... "
            time.sleep(5)
        i = i + 1
    releasePhone(phone)
    return 0


def releasePhone(phone):
    response = urllib2.urlopen(
        "http://api.ixinsms.com/api/do.php?action=cancelRecv&sid=1257" + "&phone=" + phone + "&token=" + token)
    html = response.read()
    result = html.split('|')
    if result[0] == '1':
        print "[3]release:" + phone
        return result[1]
    else:
        print "[3]release error"
