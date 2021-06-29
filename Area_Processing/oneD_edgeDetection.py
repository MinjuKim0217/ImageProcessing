import cv2
import numpy as np
from matplotlib import pyplot as plt
img = cv2.imread('ckt_ori.jpg') 
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

roberts_x = np.array([[-1, 0, 0], [0, 1, 0], [0, 0, 0]]) 
roberts_y = np.array([[0, 0, -1], [0, 1, 0], [0, 0, 0]]) 
prewitt_x = np.array([[-1, -1, -1], [0, 0, 0], [1, 1, 1]]) 
prewitt_y = np.array([[1, 0, -1], [1, 0, -1], [1, 0, -1]]) 
sobel_x = np.array([[-1, -2, -1], [0, 0, 0], [1, 2, 1]]) 
sobel_y = np.array([[1, 0, -1], [2, 0, -2], [1, 0, -1]])

roberts_x = cv2.convertScaleAbs(cv2.filter2D(gray, -1, roberts_x)) 
roberts_y = cv2.convertScaleAbs(cv2.filter2D(gray, -1, roberts_y)) 
prewitt_x = cv2.convertScaleAbs(cv2.filter2D(gray, -1, prewitt_x)) 
prewitt_y = cv2.convertScaleAbs(cv2.filter2D(gray, -1, prewitt_y)) 
sobel_x = cv2.convertScaleAbs(cv2.filter2D(gray, -1, sobel_x)) 
sobel_y = cv2.convertScaleAbs(cv2.filter2D(gray, -1, sobel_y))

prewitt = cv2.addWeighted(prewitt_x, 1, prewitt_y, 1, 0) 
roberts = cv2.addWeighted(roberts_x, 1, roberts_y, 1, 0) 
sobel = cv2.addWeighted(sobel_x, 1, sobel_y, 1, 0)

cv2.imshow('original', gray) 
cv2.imshow('roberts', roberts) 
cv2.imshow('prewitt', prewitt) 
cv2.imshow('sobel', sobel) 
cv2.waitKey(0)

