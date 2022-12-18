import cv2
import numpy as np
from matplotlib import pyplot as plt
image=cv2.imread('power.png', 0)
gamma=2
gamma2=np.power(image, gamma)
gamma=3
gamma3=np.power(image, gamma)
gamma=4
gamma4=np.power(image, gamma)
plt.subplot(141), plt.imshow(image, 'gray'), plt.title('original')
plt.subplot(142), plt.imshow(gamma2, 'gray'), plt.title('gamma=2')
plt.subplot(143), plt.imshow(gamma3, 'gray'), plt.title('gamma=3')
plt.subplot(144), plt.imshow(gamma4, 'gray'), plt.title('gamma=4')
plt.show()