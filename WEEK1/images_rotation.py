#! /usr/bin/env python3

import os, sys

from PIL import Image

size = (128, 128)
new_dir="/opt/icons/"
img_dir="images/"

with os.scandir(img_dir) as entries: #python 3.5 en la VM, tuve que cambiarlo en el script
    for entry in entries:
        out_file = new_dir + entry.name + ".jpeg"
        #print(entry.name, out_file)
        in_file = img_dir + entry.name
        try:
            with Image.open(in_file) as im:
                im.thumbnail(size)
                out = im.rotate(270) # degrees counter-clockwise
                out.convert('RGB').save(out_file, format="JPEG")
        except OSError as e:
            print("cannot convert", img_dir+entry.name, out_file)
            print (e)
            continue

    
'''
for infile in sys.argv[1:]:
    f, e = os.path.splitext(infile)
    outfile = f + ".jpg"
try:
            with Image.open(infile) as im:
                im.thumbnail(size)
                out = im.rotate(45) # degrees counter-clockwise
                im.save(outfile)
        except OSError:
            print("cannot convert", infile)
            continue


'''