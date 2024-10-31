import cv2, sys, unicodedata
from PIL import ImageFont, ImageDraw, Image
from matplotlib import pyplot as plt
import numpy as np

args = sys.argv
if len(args) < 2:
    raise ValueError
filepath = args[1]

img = Image.fromarray(cv2.cvtColor(cv2.imread(filepath), cv2.COLOR_BGR2RGB))
img.save(filepath.split(".")[0] + ".webp")