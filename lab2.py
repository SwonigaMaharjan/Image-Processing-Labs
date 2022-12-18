import cv2
import numpy as np
from matplotlib import pyplot as plt
image1=cv2.imread('lab2image1.png')
image2=cv2.imread('lab2image2.png')
img1=cv2.resize(image1,(256,256))
img2=cv2.resize(image2,(256,256))
dest_and=cv2.bitwise_and(img2, img1, mask=None)
dest_or=cv2.bitwise_or(img2, img1, mask=None)
dest_xor=cv2.bitwise_xor(img2, img1, mask=None)
dest_not=cv2.bitwise_not(img2, mask=None)
plt.subplot(231), plt.imshow(img1), plt.title('Image 1')
plt.subplot(232), plt.imshow(img2), plt.title('Image 2')
plt.subplot(233), plt.imshow(dest_and), plt.title('Bitwise AND')
plt.subplot(234), plt.imshow(dest_or), plt.title('Bitwise OR')
plt.subplot(235), plt.imshow(dest_xor), plt.title('Bitwise XOR')
plt.subplot(236), plt.imshow(dest_not), plt.title('Bitwise NOT')
plt.show()