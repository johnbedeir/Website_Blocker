#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Aug  2 03:56:56 2020

@author: triple-a
"""

import time
from datetime import datetime as dt

hosts_path="C:\Windows\System32\drivers\etc\hosts"
redirect="127.0.0.1"
website_list=["facebook.com", "www.facebook.com"]

while True:
    if dt(dt.now().year, dt.now().month, dt.now().day,8) < dt.now() < dt(dt.now().year, dt.now().month, dt.now().day,16):
        print("Working Time...")
        with open(hosts_path, 'r+') as file:
            content=file.read()
            for websites in website_list:
                if websites in content:
                    pass
                else:
                    file.write(redirect+" "+websites+"\n")
    else:
        with open(hosts_path, 'r+') as file:
            content=file.readlines()
            file.seek(0)
            for line in content:
                if not any(websites in line for websites in website_list):
                    file.write(line)
                    file.truncate()
                else:
                    pass
        print("Fun hours...")    
    time.sleep(5)
