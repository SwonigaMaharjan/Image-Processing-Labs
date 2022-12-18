#30th July 021
#Gaussian noise addition in an Image
import cv2
import numpy as np
from matplotlib import pyplot as plt
image = cv2.imread("camera.png", 0)
row, col=image.shape
print(image.shape)
gauss=np.random.normal(10, 10, (row, col))
noisy=image+gauss

plt.subplot(131),plt.imshow(image, cmap='gray'),plt.title('Original Image')
plt.xticks([]),plt.yticks([])
plt.subplot(132),plt.imshow(noisy, cmap='gray'),plt.title('Gaussian Noise Image')
plt.xticks([]),plt.yticks([])
plt.subplot(133),plt.hist(noisy.ravel(), 256, [0, 256]),plt.title('Noisy Image Histogram')
plt.xticks([]),plt.yticks([])
plt.show()