
import cv2
import numpy as np

import cv2

cap = cv2.VideoCapture(0)
while(True):
    ret, frame = cap.read()
    gray = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    gray = cv2.medianBlur(gray,5)

    # extract region of interest
    rows = gray.shape[0]

    # find circles:
    circles = cv2.HoughCircles(gray,cv2.HOUGH_GRADIENT,1,rows/8,
                               param1=100,param2=30,
                               minRadius =1,maxRadius=30)
    




    cv2.imshow('frame', frame)
    cv2.imshow('gray', gray)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
cap.release()
cv2.destroyAllWindows()