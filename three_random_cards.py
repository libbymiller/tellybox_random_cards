# -*- coding: utf-8 -*-

# picks three random cards from each of three buckets
# combined and displays them

import os
import sys
from PIL import Image
from random import randint

num_cards = 179

prefix = "images"
folder="images"

# get random form each bucket
# in this case the middle set is some joining words

file1_int = randint(15,int(num_cards/2))
file2_int = randint(0,14)
file3_int = randint(int(num_cards/2),num_cards)

# create filename

file1 = folder+"/"+prefix+"_"+str(file1_int)+".png"
file2 = folder+"/"+prefix+"_"+str(file2_int)+".png"
file3 = folder+"/"+prefix+"_"+str(file3_int)+".png"

# combine them together

images = map(Image.open, [file1, file2, file3])
widths, heights = zip(*(i.size for i in images))

total_width = sum(widths)
max_height = max(heights)

new_im = Image.new('RGB', (total_width, max_height))

x_offset = 0
for im in images:
  new_im.paste(im, (x_offset,0))
  x_offset += im.size[0]

# save the new image

fn = prefix+'_three.jpg'
new_im.save(fn)

# save the generated image

print "saving new image - "+fn

# open in the system image viewer

os.system("open "+fn)
