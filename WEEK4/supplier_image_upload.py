#!/usr/bin/env python3

import requests

url='http:// /upload/'

img_dir = "supplier-data/images/"

entries = [fn for fn in os.listdir(img_dir) if fn.endswith('.jpeg')]

for entry in entries:
    with open(img_dir+entry, 'rb') as im:
        r=request.post(url, files={'file': im})