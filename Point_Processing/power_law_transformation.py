import cv2 
import numpy as np
import matplotlib.pyplot as plt
import cv2 
import numpy as np
import matplotlib.pyplot as plt
#Plotting Images
titles = ['Original img','gamma = 0.1','gamma = 0.5','gamma = 1.5','gamma = 2.5','gamma = 10','gamma = 20']

for i in range(7):
    plt.subplot(3,3,i+1),plt.imshow(images[i])
    plt.title(titles[i])
    plt.xticks([]),plt.yticks([])

plt.show()
