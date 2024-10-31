import cv2, sys, unicodedata
from PIL import ImageFont, ImageDraw, Image
from matplotlib import pyplot as plt
import numpy as np

def get_east_asian_width_count(text):
    count = 0
    for c in text:
        if unicodedata.east_asian_width(c) in 'FWA':
            count += 2
        else:
            count += 1.15
    return count

args = sys.argv
b = 0
if len(args) < 3:
    raise ValueError
for i, arg in enumerate(args[1:]):
    if i == 0:
        filepath = arg
    elif i == 1:
        text = arg
    elif arg == "-w":
        b = 255

img = cv2.imread(filepath)
overlay = img.copy()
cv2.rectangle(overlay, (0, 246), (640, 246+90), (b, b, b), thickness=-1)
mat_img = cv2.addWeighted(overlay, 0.75, img, 0.25, 0)

size = get_east_asian_width_count(text)
fontpath = 'C:\Windows\Fonts\meiryob.ttc'
font = ImageFont.truetype(fontpath, min(90*3//4, int(600*2//size)))
img_pil = Image.fromarray(cv2.cvtColor(mat_img, cv2.COLOR_BGR2RGB))
draw = ImageDraw.Draw(img_pil)
draw.text(((640-font.size*size/2)/2, 246+(90-font.size*4/3)/2), text, font=font , fill=(255-b, 255-b, 255-b, 255))
result = np.array(img_pil)

img_pil.save(filepath.split(".")[0] + "_thumb.webp")
plt.imshow(result)
plt.show()