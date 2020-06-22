#!/usr/bin/env python3

import os
from PIL import Image

oldpath = os.path.expanduser('~') + '/images/'
newpath = '/opt/icons/'

for image in os.listdir(oldpath):
    print(image)
    if '.' not in image[0]:
        fixed_image = Image.open(oldpath + image)
        fixed_image.rotate(-90).resize((128, 128)).convert("RGB").save(newpath + image.split('.')[0], 'jpeg')
        fixed_img.close()
#NB:dont save this file or any other file in the images folder that will lead to the program crashing
#if you want to save any file othe than an image in images folder then edit the for and if loop conditions 
