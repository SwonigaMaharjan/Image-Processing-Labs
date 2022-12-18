import cv2
from matplotlib import pyplot as plt
import numpy as np
img=cv2.imread('low contrast image.jpg',0)
img_1 = cv2.resize(img, (256,256))
equ=cv2.equalizeHist(img_1)
res = np.hstack((img_1,equ)) #stacking images side-by-side
cv2.imshow('res.png',res)
histr=cv2.calcHist([img_1], [0], None, [256], [0, 256])
histr1=cv2.calcHist([equ], [0], None, [256], [0, 256])
plt.plot(histr)
plt.plot(histr1)
plt.show()
cv2.waitKey(0)
cv2.destroyAllWindows()