#!/usr/bin/env python3

import os
import requests
import json
import locale


descr_dir = "supplier-data/descriptions/"
data = {}
url='http:// /upload/'


files_txt = [fn for fn in os.listdir(descr_dir) if fn.endswith('.txt')]
for file in files_txt:
    file_name, file_ext = file.split('.')
    with open(descr_dir+file, 'r') as fl:
        name = fl.readline().rstrip('\n')
        weight = locale.atoi(fl.readline().rstrip(' lbs\n'))
        description = fl.read().rstrip('\n')
        image_name = file_name + '.jpeg'
    data['name'] = name
    data['weight'] = weight
    data['description'] = description
    data['image_name'] = image_name
    #print(json.dumps(data))
    r=request.post(url, data = json.dumps(data))





