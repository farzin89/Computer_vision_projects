
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
    #Drow on top of them

    if circles is not None:
        circles =np.uint16(np.around(circles))
        for i in circles[0,:]:
            center = (i[0],i[1])
            # Circle centre
            cv2.circle(frame,center,1,(0,100,100) ,3)
            #circle outline
            radius = i[2]
            cv2.circle(frame,center,radius,(255,0,255),3)





    cv2.imshow('frame', frame)
    #cv2.imshow('gray', circles)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
cap.release()
cv2.destroyAllWindows()