import numpy as np
import cv2
from matplotlib import pyplot as plt
import cPickle as pickle
from sklearn.externals import joblib
from image_transformation import apply_image_transformation
print('Processing....')
clf= joblib.load('./modules/model-serialized-logistic.pkl')


cap = cv2.VideoCapture(0)

while(True):
    # Capture frame-by-frame
    ret, frame = cap.read()

    # Our operations on the frame come here
    gray = frame#cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    cv2.rectangle(gray,(250,250),(450,450),(0,255,0),3)
    # Display the resulting frame
    plt.imshow(gray)
    
    detect= gray[250:450,250:450]
    fr= apply_image_transformation(detect)
    frame_flattened=frame.flatten()
    predicted_labels= clf.predict(np.reshape(frame_flattened,(1,frame_flattened.size)))
    predicted_label = predicted_labels[0]
    print(predicted_label)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# When everything done, release the capture
cap.release()
cv2.destroyAllWindows()