# -*- coding: utf-8 -*-
"""
Created on Sat Jul 14 15:19:43 2018

@author: Python
"""
import re
import requests


def getInfo(key,length):
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64; rv:45.0) Gecko/20100101 Firefox/45.0",
    }
    if length == 4:
        # 通过抓包的方式获取的url，并不是浏览器上显示的url
        url = "http://www.chengyugushi.net/plus/search.php?kwtype=0&q="+str(key)+"&searchtype=title"
        # 这里的headers及formdata是从浏览器中获取到的
        response = requests.get(url, headers).text
        potten = "<font color='red'><font color='red'>[\s\S]*?</font></font>[\s\S]*?</font></font>([\s\S]*?)\r"
        word = re.findall(potten, response)
        if not word:
            return '没有该四字成语'
        return word[0][1:]
    elif length == 5:
        # 通过抓包的方式获取的url，并不是浏览器上显示的url
        url = "http://www.chengyugushi.net/plus/search.php?kwtype=0&q="+str(key)+"&searchtype=title"
        # 这里的headers及formdata是从浏览器中获取到的
        response = requests.get(url, headers).text
        potten = "<font color='red'><font color='red'>[\s\S]*?</font></font>[\s\S]*?</font></font>([\s\S]*?)\r"
        word = re.findall(potten, response)
        if not word:
            return '没有该五字成语'
        return word[0][1:]
    elif length == 6:
        # 通过抓包的方式获取的url，并不是浏览器上显示的url
        url = "http://www.chengyugushi.net/plus/search.php?kwtype=0&q="+str(key)+"&searchtype=title"
        # 这里的headers及formdata是从浏览器中获取到的
        response = requests.get(url, headers).text
        potten = "<font color='red'><font color='red'>[\s\S]*?</font></font>[\s\S]*?</font></font>([\s\S]*?)\r"
        word = re.findall(potten, response)
        if not word:
            return '没有该六字成语'
        return word[0][1:]
    elif length == 8:
        # 通过抓包的方式获取的url，并不是浏览器上显示的url
        url = "http://www.chengyugushi.net/plus/search.php?kwtype=0&q="+str(key)+"&searchtype=title"
        # 这里的headers及formdata是从浏览器中获取到的
        response = requests.get(url, headers).text
        potten = "<font color='red'><font color='red'>[\s\S]*?</font></font>[\s\S]*?</font></font>([\s\S]*?)\r"
        word = re.findall(potten, response)
        if not word:
            return '没有该八字成语'
        return word[0][1:]


def youdao(key,length):
    return getInfo(key,length)

# key = input('请输入:')
# length = 4
# print(youdao(key,length))