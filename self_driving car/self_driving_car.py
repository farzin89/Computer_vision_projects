import cv2
import numpy as np
import matplotlib.pyplot as plt

def canny(image):
    #convert to gray
    gray = cv2.cvtColor(lane_image,cv2.COLOR_RGB2GRAY)
    #convert to blur
    blur = cv2.GaussianBlur(gray,(5,5),0)
    #apply canny to reduce the noice
    canny = cv2.Canny(blur,50,150)
    return canny

def region_of_interest(image):
    height = image.shape[0]
    polygons = np.array([[(200,height),(1100,height),(550,250)]])
    mask = np.zeros_like(image)
    cv2.fillPoly(mask,polygons,255)
    return mask



image = cv2.imread('road.JPG')
lane_image = np.copy(image)
canny = canny(lane_image)




cv2.imshow('result',region_of_interest(canny))
cv2.waitKey(0)