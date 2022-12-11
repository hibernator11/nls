#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Dec 11 10:07:19 2022

@author: gustavo
"""

import requests

filename = "../assessment/nbs-uris-list.txt"

urls = []
errors = 0
with open(filename) as file:
    urls = [line.rstrip() for line in file]

for idx,url in enumerate(urls,1):
    r = requests.head(url + ".html")
  
    if r.status_code == 200:
        print(f'{idx}) {url} was found')
    elif r.status_code == 301: 
        print(f'{idx}) {url} was redirected')
    else:
        print(f'{idx}) {url} was NOT found')
        errors = errors +1
print("Errors:" + str(errors))