from scipy import misc
import numpy as np
import csv

image = misc.imread('image.jpeg')
vector = image.flatten()

resultFile = open('image_vector.csv', 'wb')
wr = csv.writer(resultFile)

for val in vector:
	wr.writerow([val])