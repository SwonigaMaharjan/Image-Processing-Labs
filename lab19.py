#27th June 021
#Implementation of Gaussian Low Pass Filter
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
H3=np.exp(((-1)*(D**2))/(2*((cutoff[1])**2)))
G3=H3*fourier_image
imback2=np.fft.ifft2(G3)
imback2=np.uint8(np.real(imback2))
imback2[imback2>=225]=0

#cutoff=10
H4=np.exp(((-1)*(D**2))/(2*((cutoff[3])**2)))
G4=H4*fourier_image
imback3=np.fft.ifft2(G4)
imback3=np.uint8(np.real(imback3))
imback3[imback3>=225]=0

#cutoff=20
H5=np.exp(((-1)*(D**2))/(2*((cutoff[2])**2)))
G5=H5*fourier_image
imback4=np.fft.ifft2(G5)
imback4=np.uint8(np.real(imback4))
imback4[imback4>=225]=0

plt.subplot(221),plt.imshow(image, cmap='gray'),plt.title('Original Image')
plt.xticks([]),plt.yticks([])
plt.subplot(222),plt.imshow(imback2, cmap='gray'),plt.title('Cutoff=40')
plt.xticks([]),plt.yticks([])
plt.subplot(223),plt.imshow(imback3, cmap='gray'),plt.title('Cutoff=10')
plt.xticks([]),plt.yticks([])
plt.subplot(224),plt.imshow(imback4, cmap='gray'),plt.title('Cutoff=20')
plt.xticks([]),plt.yticks([])
plt.show()
cv2.waitKey(0)