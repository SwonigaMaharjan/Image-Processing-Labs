#lab5: Power Law Transformation of an Image
import cv2
import numpy as np
from matplotlib import pyplot as plt
input=cv2.imread('fractured.png',0)
gamma = 2
gamma_2= np.power(input,gamma)
gamma = 3
gamma_3= np.power(input,gamma)
gamma = 4
gamma_4= np.power(input,gamma)
titles = ['Input Image', 'Gamma=2','Gamma=3', 'Gamma=4']
images = [input, gamma_2, gamma_3, gamma_4]
for i in range(4):
    plt.subplot(1,4,i+1),plt.imshow(images[i], 'gray')
    plt.title(titles[i])
    plt.xticks([]),plt.yticks([])
plt.show()