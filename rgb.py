# coding: utf-8
from scipy import misc
import numpy as np
image=misc.imread('chopper.jpg')
print(image)
print(image.shape)
print(image[0][0])
import matplotlib.pyplot as plt
plt.imshow(image)
plt.show()
def average(pixel):
    return (pixel[0]+pixel[1]+pixel[2])/3
grey=np.zeros((image.shape[0],image.shape[1]))
for rownum in range(len(image)):
    for colnum in range(len(image[rownum])):
        grey[rownum][colnum]=average(image[rownum][colnum])
        
import matplotlib.cm as cm
plt.imshow(grey,cmap=cm.Greys_r)
plt.show()
misc.imsave('chopper-grey.jpg',grey)
