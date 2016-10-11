import json
import re
import random
from pprint import pprint
import PIL
from PIL import ImageFont
from PIL import Image
from PIL import ImageDraw
import textwrap


lists = {}
cards = {}

font = ImageFont.truetype("Arial.ttf",50)
width = 350
height = 500
prefix = "images"
folder = "images"

with open('trello.json') as data_file:    
    data = json.load(data_file)

for list in data["lists"]:
  lists[list["id"]] = list["name"]
  cards[list["name"]] = []


for card in data["cards"]:
  nameOfList = lists[card["idList"]]
  if(nameOfList!="...."):
    name = card["name"]
    name = re.sub(r"\<", "less than", name)
    name = re.sub(r"\<", "more than", name)
    cards[nameOfList].append(name)


fn = "cards.csv"
lastType = None
colour = None

# Open a file
fo = open(fn, "w")

count = 0

# loop through the joining words

arr = ["and","and","and","and","and","or","or","or","or","or","but","but","but","but","but"]
for name in arr: 
      ttype = "join"

      # random colour
      colour = "#%06x" % random.randint(0, 0xFFFFFF)

      towrite = '"'+name+'",'+"'"+ttype+'",'+colour+'",\n'

      # write the line to the csv

      fo.write(towrite)

      # create an image

      img=Image.new("RGBA", (width,height),colour)
      draw = ImageDraw.Draw(img)
      text = str(name)
      margin = 40
      offset = 150
      draw.text((margin, offset), text, font=font, fill="#ffffff")
      draw = ImageDraw.Draw(img)
      ifn = folder+"/"+prefix+"_"+str(count)+".png"
      print "saving new image "+ifn+" text "+text
      img.save(ifn)
      count = count +1

for ttype,names in cards.iteritems():
   names = cards.get(ttype)
   for name in names:
      colour = "#%06x" % random.randint(0, 0xFFFFFF)
      towrite = '"'+name+'",'+"'"+ttype+'",'+colour+'",\n'
      fo.write(towrite)

      #font = ImageFont.truetype("Arial.ttf",50)
#      img=Image.new("RGBA", (350,500),colour)
      img=Image.new("RGBA", (width,height),colour)
      draw = ImageDraw.Draw(img)
      margin = 40
      offset = 150
      text = str(name)
      for line in textwrap.wrap(text, width=11):
         draw.text((margin, offset), line, font=font, fill="#ffffff")
         offset += font.getsize(line)[1]
      draw = ImageDraw.Draw(img)
      ifn = folder+"/"+prefix+"_"+str(count)+".png"
      print "saving new image "+ifn+" text "+text
      img.save(ifn)
      count = count +1

# close file
fo.close()

print "done writing to "+fo.name

# for each of these, create an image file




colour = "#563aaa"

# font = ImageFont.truetype("Arial-Bold.ttf",14)

