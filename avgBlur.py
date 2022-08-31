import numpy
import argparse
import cv2
import os

image = cv2.imread('hd1.jpeg')
path3 = './image_median'

for i in range(10):
    j = i+1
    # 4 method 
    blur = cv2.blur(image, (3*j,3*j))          #  average
    j = str(j)
    if not os.path.exists(path3):
        os.makedirs(path3)
    
    cv2.imwrite(path3 + "/image" + j + ".jpeg",blur)