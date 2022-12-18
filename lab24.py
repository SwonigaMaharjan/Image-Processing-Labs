#30th July 021
#Denoising of an Image
import cv2
from matplotlib import pyplot as plt
image = cv2.imread("birdNoise.jpg")
dst=cv2.fastNlMeansDenoisingColored(image, None, 10, 10, 7, 21)
plt.subplot(121),plt.imshow(image)
plt.subplot(122),plt.imshow(dst)
plt.show()