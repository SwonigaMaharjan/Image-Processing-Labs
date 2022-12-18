#9th June 021
#Sharpening an image(High Pass Filter)
import cv2
import numpy as np
from matplotlib import pyplot as plt
image = cv2.imread("eye.jpg")
gauss_mask = cv2.GaussianBlur(image,(9,9),10.0)
image_sharp = cv2.addWeighted(image, 2, gauss_mask, -1, 0)
#high pass kernel 3x3
kernel=np.array([[-1, -1, -1],
                 [-1, 8, -1],
                 [-1, -1, -1]])
#ig_hpf = image- gauss_mask
image_hpf = cv2.filter2D(image, -1, kernel)
plt.subplot(131),plt.imshow(image),plt.title('Original')
plt.xticks([]),plt.yticks([])
plt.subplot(132),plt.imshow(image_hpf),plt.title('Mask')
plt.xticks([]),plt.yticks([])
plt.subplot(133),plt.imshow(image_sharp),plt.title('sharpened')
plt.xticks([]),plt.yticks([])
plt.show()
cv2.waitKey(0)