#Lab 27:Image Segmentation
import cv2
import numpy as np
from matplotlib import pyplot as plt

img = cv2. imread('sc.png')
gray = cv2. cvtColor(img,cv2. COLOR_BGR2GRAY)
ret, thresh = cv2.threshold(gray, 0, 255,cv2. THRESH_BINARY_INV+cv2. THRESH_OTSU)

# Noise removal using Morphological 
# closing operation 
kernel = np.ones((3, 3), np.uint8) 
closing = cv2.morphologyEx(thresh, cv2.MORPH_CLOSE,kernel, iterations = 2) 
  
# Background area using Dialation 
bg = cv2.dilate(closing, kernel, iterations = 1) 
  
# Finding foreground area 
dist_transform = cv2.distanceTransform(closing, cv2.DIST_L2, 0) 
ret, fg = cv2.threshold(dist_transform, 0.02* dist_transform.max(), 255, 0) 
  
plt.subplot(121),plt.imshow(img,cmap = 'gray')
plt.title('Original'), plt.xticks([]), plt.yticks([])
plt.subplot(122),plt.imshow(fg,cmap = 'gray')
plt.title('Image'), plt.xticks([]), plt.yticks([])
plt.show()
