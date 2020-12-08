#!/usr/bin/env python3

import requests
import os

url='http://35.184.104.167/upload/'

img_dir = "supplier-data/images/"

entries = [fn for fn in os.listdir(img_dir) if fn.endswith('.jpeg')]

for entry in entries:
    with open(img_dir+entry, 'rb') as im:
        r = requests.post(url, files={'file': im})