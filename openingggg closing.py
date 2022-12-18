import numpy as np
import cv2
from matplotlib import pyplot as plt

image = cv2.imread('openClose.png',0)
kernel = np.ones((13,13), np.uint8)
opening = cv2.morphologyEx(image, cv2.MORPH_OPEN, kernel)
closing = cv2.morphologyEx(image, cv2.MORPH_CLOSE, kernel)

plt.subplot(131), plt.imshow(image, 'gray'), plt.title('Original')
plt.subplot(132), plt.imshow(opening, 'gray'), plt.title('Opening')
plt.subplot(133), plt.imshow(closing, 'gray'), plt.title('Closing')
plt.show()
