import numpy as numpy
import cv2
import os

import face_recognition as fr
#print(fr)

test_img=cv2.imread(r'C:\Users\ELCOT\AppData\Local\Programs\Python\Python38-32\face detection\test1.jpg')
faces_detected,gray_img=fr.faceDetection(test_img)

print("Face Detected: ",faces_detected)

#training will begin from here

faces,faceID=fr.labels_for_training_data(r'C:\Users\ELCOT\AppData\Local\Programs\Python\Python38-32\face detection\dataset\image')
face_recognizer=fr.train_Classifier(faces,faceID)
face_recognizer.save(r'C:\Users\ELCOT\AppData\Local\Programs\Python\Python38-32\face detection\dataset\trainingData.yml')

name={0:'priya'}

for face in faces_detected:
    (x,y,w,h)=face
    roi_gray=gray_img[y:y+h,x:x+h]
    label,confidence=face_recognizer.predict(roi_gray)
    print("label:",label)
    print("confidence:",confidence)
    fr.draw_rect(test_img,face)
    predict_name=name[label]
    fr.put_text(test_img,predict_name,x,y)

resized_img=cv2.resize(test_img,(1000,700))

cv2.imshow(' ',resized_img)
cv2.waitKey(0)
cv2.destroyAllWindows

