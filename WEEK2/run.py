#! /usr/bin/env python3

import os, sys
import json
import requests
from pprint import pprint

FB_PATH = '/data/feedback/'
SITE_IP = 'http://34.70.208.246'

dir_files = []
fb_list = []
title, name, fb_date, feedback = '', '', '', ''

dir_files = os.listdir(FB_PATH)

#print(dir_files)

for file in dir_files:
    with open(FB_PATH + file, 'r') as fb:
        title = fb.readline()
        name = fb.readline()
        fb_date = fb.readline()
        feedback = fb.read()
        foo = {'title': title,
               'name': name,
               'date': fb_date,
               'feedback': feedback }
        #print(foo)
        response = requests.post(SITE_IP + '/feedback/', data=foo)
        #print(response.request.url, response.request.body, str(response.ok) )
        response.raise_for_status()



    
