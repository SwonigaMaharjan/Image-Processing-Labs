import cv2
import numpy as np
from matplotlib import pyplot as plt

image = cv2.imread('dft.png')
c = 255/np.log(1+np.max(image))
log_image = c*(np.log(image+1))
log_image = np.array(log_image,dtype = np.uint8)

plt.subplot(121), plt.imshow(image, 'gray'), plt.title('Original')
plt.subplot(122), plt.imshow(log_image, 'gray'), plt.title('Log Image')
plt.show()
