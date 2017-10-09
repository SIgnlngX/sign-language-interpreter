# coding: utf-8
# We are going to ocnvert a RGB image into a grayscale image. For your image, just enter the name of image in place of 'image'
# Import necessary packages
from scipy import misc
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.cm as cm

# Loading the image using misc
image=misc.imread('image.jpg')

# Printing the image and the shape
print(image)
print(image.shape)
print(image[0][0])
plt.imshow(image)
plt.show()

# Now we will use weighted average to convert a RGB pixel into grayscale. We can use simple average but this makes the image more 'human'
def weightedAverage(pixel):
    return (0.299*pixel[0]+0.587*pixel[1]+0.114*pixel[2])

grey=np.zeros((image.shape[0],image.shape[1])) # 2D numpy array
for rownum in range(len(image)): # get row number
    for colnum in range(len(image[rownum])):
        grey[rownum][colnum]= weightedAverage(image[rownum][colnum])
        
# Display the image
plt.imshow(grey,cmap=cm.Greys_r)
plt.show()
# Saving image
misc.imsave('image-grey.jpg',grey)
