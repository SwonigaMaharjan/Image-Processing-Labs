#17th June 021
#To plot the magnitude spectrum
import cv2
import numpy as np
from matplotlib import pyplot as plt
image = cv2.imread("camera.png", 0)
image_float32=np.float32(image)
dft=cv2.dft(image_float32, flags=cv2.DFT_COMPLEX_OUTPUT)
dft_shift=np.fft.fftshift(dft)
magnitude_spectrum=20*np.log(cv2.magnitude(dft_shift[:, :, 0], dft_shift[:, :, 1]))
plt.subplot(121),plt.imshow(image, cmap='gray'),plt.title('Input Image')
plt.xticks([]),plt.yticks([])
plt.subplot(122),plt.imshow(magnitude_spectrum, cmap='gray'),plt.title('Magnitude Spectrum')
plt.xticks([]),plt.yticks([])
plt.show()
cv2.waitKey(0)