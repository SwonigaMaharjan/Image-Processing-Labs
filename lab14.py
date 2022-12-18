#13th Jun 021
#Erosion and Dilation of an Image
import cv2
import numpy as np
from matplotlib import pyplot as plt
image=cv2.imread('erosionDilation.png', 0)
kernel=np.ones((5, 5), np.uint8)
erosion=cv2.erode(image, kernel, iterations=1)
dilation=cv2.dilate(image, kernel, iterations=1)
plt.subplot(131), plt.imshow(image, 'gray'), plt.title('ORIGINAL')
plt.subplot(132), plt.imshow(erosion, 'gray'), plt.title('EROSION')
plt.subplot(133), plt.imshow(dilation, 'gray'), plt.title('DILATION')
plt.show()