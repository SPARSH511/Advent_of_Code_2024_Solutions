import os
import numpy as np
from PIL import Image

dir = os.path.dirname(os.path.abspath(__file__))
infile = dir+"\\input.txt"

s = open(infile).read().strip().split("\n")
s = [i.replace("p=","").replace("v=","").split() for i in s]
s = [[tuple(map(int,i.split(','))) for i in item] for item in s]

# m,n = 101,103
# for simulation_time in range(m*n):
#     test_pic = [[0]*n for _ in range(m)] # Black(0) color for all pixels before
#     for item in s:
#         x,y = item[0]
#         vx,vy = item[1]
#         x = (x+simulation_time*vx)%m
#         y = (y+simulation_time*vy)%n
#         test_pic[x][y] = 255 # White(255) color for selected pixels
#     # Ensure image is a valid grayscale 3D array
#     image = Image.fromarray(np.array(test_pic, dtype=np.uint8), 'L')
#     # Resize the image (scale by 5x)
#     bigger_image = image.resize((n * 5, m * 5), Image.NEAREST)
#     # Save the resized image
#     bigger_image.save(os.path.join(dir, "test_images", f"{simulation_time}.png"))

# After manual identification of images 
print("Answer to Problem 2 :", 7858)

