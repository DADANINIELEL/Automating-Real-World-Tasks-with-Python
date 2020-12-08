#!/usr/bin/env python3

import os
import sys

from PIL import Image

size = (600, 400)


img_dir = "supplier-data/images/"

entries = [fn for fn in os.listdir(img_dir) if fn.endswith('.tiff')]
print (entries)
for entry in entries:
    file_name, file_ext = entry.split('.')
    print('processing: ' + entry)
    try:
        with Image.open(img_dir + entry) as im:
            out = im.convert('RGB')
            out.thumbnail(size)
            out.save(img_dir + file_name+'.jpeg', format="JPEG")
    except OSError as e:
        print("cannot convert ", entry)
        print(e)
        continue


# if __name__ == "__main__":
#      main(sys.argv)
