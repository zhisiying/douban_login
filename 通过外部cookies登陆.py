#!/usr/bin/env python
# encoding: utf-8
"""
@version: python3.6
@author: zsy
@contact: 643424678@qq.com
@software: PyCharm
@file: 通过外部cookies登陆.py
@time: 2018/4/20/020 11:27
"""

import requests

cookie = {}
cookie_str = 'bid=p5VNmmSxy08; __yadk_1.2.197568178.1=1; ck=:Wz43jo2Ymhc'
for line in cookie_str.split(';'):
    key, value = line.split('=', 1)
    cookie[key] = value

urls = requests.get('https://www.douban.com/', cookies=cookie).text
print(urls)
