import cv2
import numpy as np

cascades_face = "cascades/haarcascade_frontalface_default.xml"
cascades_eyes = 'cascades/haarcascade_eye.xml'

face_classifier = cv2.CascadeClassifier(cascades_face)
eyes_classifier = cv2.CascadeClassifier(cascades_eyes)

def face_and_eyes_detector(image):
    # convert to gray scale
    gray = cv2.cvtColor(image)

