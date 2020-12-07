#! /usr/bin/env python3

import os, sys
import json
import requests

FB_PATH = 'data/feedback/'
SITE_IP = '127.0.0.1'

dir_files = []
fb_list = []
title, name, fb_date, feedback = '', '', '', ''

dir_files = os.listdir(FB_PATH)

print(entries)

for entry in entries:
    with open(entry, 'r') as fb:
        title = fb.readline()
        name = fb.readline()
        fb_date = fb.readline()
        feedback = fb.read()
        foo = {'title': title,
               'name': name,
               'date': fb_date,
               'feedback': feedback }
        fb_list.append(foo)

print(foo)
    
