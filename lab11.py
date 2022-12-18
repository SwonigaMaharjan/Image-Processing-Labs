#10th June 021
import cv2
import numpy as np
from matplotlib import pyplot as plt
image=cv2.imread("bikesgray.jpg")
imageWob=cv2.Laplacian(image, cv2.CV_64F, ksize=1)
image=cv2.GaussianBlur(image, (3, 3), 0)
imageWb=cv2.Laplacian(image, cv2.CV_64F, ksize=1)
plt.subplot(131), plt.imshow(image), plt.title('Original')
plt.subplot(132), plt.imshow(imageWob), plt.title('Output: 2nd order Derivative w/o Blur')
plt.subplot(133), plt.imshow(imageWb), plt.title('2nd order Derivative')
plt.show()