import numpy as np
import cv2
img=cv2.imread('meme.png')
cv2.imshow('original', img)
img1=cv2.imread('meme.png', 0)
cv2.imshow('greyscale', img1)
cv2.waitKey(0)
cv2.destroyAllWindows()
print(img.shape)
print(img[:, :, 0])
print(img1.shape)
print(img1[:, :])