import matplotlib.pyplot as plt
import cv2
import numpy as np
img=cv2.imread('star.jpg')
img=cv2.cvtColor(img,cv2.COLOR_BGR2RGB)
plt.imshow(img)
plt.show()