import numpy
import argparse
import cv2
import os

image = cv2.imread('hd1.jpeg')
path1 = './image_average'

for i in range(10):
    j = i+1
    # 4 method 
    blur = cv2.medianBlur(image, 2*j+1)       #  median
    j = str(j)
    if not os.path.exists(path1):
        os.makedirs(path1)
    
    cv2.imwrite(path1 + "/image" + j + ".jpeg",blur)