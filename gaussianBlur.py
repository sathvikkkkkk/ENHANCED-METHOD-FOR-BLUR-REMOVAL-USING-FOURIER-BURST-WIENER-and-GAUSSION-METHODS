import numpy
import argparse
import cv2
import os

image = cv2.imread('hd1.jpeg')
path2 = './image_gaussian'


for i in range(10):
    j = i+1
    # 4 method 
    blur = cv2.GaussianBlur(image, (2*j+1,2*j+1), 0)   #  Gaussian
    j = str(j)
    if not os.path.exists(path2):
        os.makedirs(path2)
    
    cv2.imwrite(path2 + "/image" + j + ".jpeg",blur)