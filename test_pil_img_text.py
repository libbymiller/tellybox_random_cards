import PIL
from PIL import ImageFont
from PIL import Image
from PIL import ImageDraw
import textwrap

colour = "#563aaa"

# font = ImageFont.truetype("Arial-Bold.ttf",14)
font = ImageFont.truetype("Arial.ttf",50)
img=Image.new("RGBA", (350,500),colour)
draw = ImageDraw.Draw(img)
margin = 40
offset = 150
text = "Lorem ipsum dolor sit amet, consectetur adipisicing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum."
novo = textwrap.wrap(text, width=20)
print(novo)
for line in textwrap.wrap(text, width=15):
    draw.text((margin, offset), line, font=font, fill="#ffffff")
    offset += font.getsize(line)[1]
draw = ImageDraw.Draw(img)
img.save("a_test.png")

