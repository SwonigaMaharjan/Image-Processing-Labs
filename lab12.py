#10th June 021
import cv2
import numpy as np
from matplotlib import pyplot as plt
image=cv2.imread("bikesgray.jpg", cv2.COLOR_BGR2GRAY)
imageX=cv2.Sobel(image, cv2.CV_64F, 1, 0, ksize=1)
imageY=cv2.Sobel(image, cv2.CV_64F, 0, 1, ksize=1)
plt.subplot(131), plt.imshow(image, 'gray'), plt.title('Original')
plt.subplot(132), plt.imshow(imageX, 'gray'), plt.title('Output: Sobel X axis')
plt.subplot(133), plt.imshow(imageY, 'gray'), plt.title('Output: Sobel Y axis')
plt.show()