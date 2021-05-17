import cv2
import numpy as np
from matplotlib import pyplot as plt

def canny():
    img=cv2.imread('ckt_ori.jpg', cv2.IMREAD_GRAYSCALE)
    
    edge1=cv2.Canny(img,50,200)
    edge2=cv2.Canny(img,100,200)
    edge3=cv2.Canny(img,170,200)
    
    cv2.imshow('original', img)
    cv2.imshow('Canny1', edge1)
    cv2.imshow('Canny2', edge2)
    cv2.imshow('Canny3', edge3)
    
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    
canny()
