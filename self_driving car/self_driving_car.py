import cv2
import numpy as np

image = cv2.imread('road.JPG')
lane_image = np.copy(image)
#convert to gray
gray = cv2.cvtColor(lane_image,cv2.COLOR_RGB2GRAY)
#convert to blur
blur = cv2.GaussianBlur(gray,(5,5),0)
#apply canny to reduce the noice
canny = cv2.Canny(blur,50,150)


cv2.imshow('result',canny)









cv2.waitKey(0)