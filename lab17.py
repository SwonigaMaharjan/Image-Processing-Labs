#24th June 021
#Implementation of Ideal Low Pass Filter
import cv2
import numpy as np
from matplotlib import pyplot as plt
image = cv2.imread("original image.png", 0)
min=np.minimum(image.shape[0], image.shape[1])
image=cv2.resize(image, (min, min))
image[image>=225]=0
M, N=image.shape
fourier_image=np.fft.fft2(image)
u=np.array(range(0, M))
v=np.array(range(0, N))
idx=np.where(u>(M/2))
u[idx]-=M
idy=np.where(v>(N/2))
v[idy]-=N
[V, U]=np.meshgrid(v, u)
D=(U**2+V**2)**(1/2)
cutoff=[50, 40, 20, 10]

#cutoff=40
H=(D<=40)
G=H*fourier_image
imback=np.fft.ifft2(G)
imback=np.uint8(np.real(imback))
imback[imback>=225]=0

#cutoff=20
H1=(D<=20)
G1=H1*fourier_image
imback1=np.fft.ifft2(G)
imback1=np.uint8(np.real(imback))
imback1[imback1>=225]=0

fshift=np.fft.fftshift(fourier_image)
magnitude_spectrum=20*np.log(np.abs(fshift))

plt.subplot(221),plt.imshow(image, cmap='gray'),plt.title('Input Image')
plt.xticks([]),plt.yticks([])
plt.subplot(222),plt.imshow(imback, cmap='gray'),plt.title('Cutoff=40')
plt.xticks([]),plt.yticks([])
plt.subplot(223),plt.imshow(imback1, cmap='gray'),plt.title('Cutoff=20')
plt.xticks([]),plt.yticks([])
plt.subplot(224),plt.imshow(magnitude_spectrum, cmap='gray'),plt.title('Magnitude Spectrum')
plt.xticks([]),plt.yticks([])
plt.show()
cv2.waitKey(0)