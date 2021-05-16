import cv2
 
# Load the image
image = cv2.imread("D:/downloads/kang.jpg")
# Blur the image
gauss = cv2.GaussianBlur(image, (7,7), 0)
# Apply Unsharp masking
unsharp_image = cv2.addWeighted(image, 2, gauss, -1, 0)
