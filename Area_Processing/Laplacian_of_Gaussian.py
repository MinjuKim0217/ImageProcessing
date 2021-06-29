import cv2
import numpy as np
 
# Load the image in greyscale
img = cv2.imread('ckt_ori.jpg',0)
 
# Apply Gaussian Blur
blur = cv2.GaussianBlur(img,(3,3),0)
 
# Apply Laplacian operator in some higher datatype
laplacian = cv2.Laplacian(blur,cv2.CV_64F)
# But this tends to localize the edge towards the brighter side.
laplacian1 = laplacian/laplacian.max()

cv2.imshow('a7',laplacian1)
cv2.waitKey(0)

# But this tends to localize the edge towards the brighter side.
laplacian1 = laplacian/laplacian.max()
 
cv2.imshow('a7',laplacian1)
cv2.waitKey(0)
