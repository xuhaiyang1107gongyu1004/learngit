# -*- coding: utf-8 -*-
"""
Created on Sat Jul 14 15:19:43 2018

@author: Python
"""
from django.shortcuts import render, redirect
import re
import requests
import datetime
from urllib import request
from lxml import etree


def getTInfo(from1, to, day=0):

    today = datetime.date.today()
    print(today)
    # 这里的headers及formdata是从浏览器中获取到的
    # ua_headers = {
    #     "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64; rv:45.0) Gecko/20100101 Firefox/45.0",
    # }
    # # 通过抓包的方式获取的url，并不是浏览器上显示的url
    # req = request.Request("http://trains.ctrip.com/TrainBooking/Search.aspx?from=" + \
    #     str(from1)+"&to="+str(to)+"&day="+str(today)+"#day="+str(day),headers = ua_headers)
    req = request.Request("http://trains.ctrip.com/TrainBooking/Search.aspx?from="+str(from1)+"&to="+str(to)+"&day="+str(today)+"#day="+str(day))
    # req.add_header("User-Agent":"Mozilla/5.0 (Windows NT 10.0; WOW64; rv:45.0) Gecko/20100101 Firefox/45.0")
    with request.urlopen(req) as f:
        print('Status:', f.status, f.reason)
        for k, v in f.getheaders():
            print('%s: %s' % (k, v))
        print('Data:', f.read().decode('utf-8'))
        # response = requests.get(url, headers = headers).text
    # response = request.urlopen(request.Request(url,headers=ua_headers)).read().decode('utf-8')
    # print(response)
    # for i in response:
    #     print(i.decode('utf-8'))
    # potten = '实时查询[\s\S]*?<div([\s\S]*?)<div class="window_pop"'
    # word = re.findall(potten, response)
    # # print(response)
    # with open('xiecheng.html', 'w') as f:
    #     for i in response:
    #         f.write(i)
    # return word[0].strip()
    # return render(request,'xiecheng.html')
    return 'ok'


def youdaoEC(from1, to):
    return getTInfo(from1, to)


from1 = input('请输入:')
to = input('请输入:')
# # day =
print(youdaoEC(from1, to))
