import os
import numpy as np
import cv2
from sklearn.externals import joblib
from image_transformation import apply_image_transformation
clf= joblib.load('./modules/model-serialized-logistic.pkl')
os.chdir('./snapshots/')
l=os.listdir('.')
l=sorted(l)
str=[]
print("Prediction: ")
for i in l:
    frame= cv2.imread(i)
    frame= apply_image_transformation(frame)
    frame_flattened=frame.flatten()
    predicted_labels= clf.predict(np.reshape(frame_flattened,(1,frame_flattened.size)))
    predicted_label = predicted_labels[0]
    str.append(predicted_label)
print(str[2:])
os.chdir('..')