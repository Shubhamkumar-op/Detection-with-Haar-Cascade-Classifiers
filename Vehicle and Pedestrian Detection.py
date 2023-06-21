import cv2
import numpy as np

# cap = cv2.VideoCapture('videos/walking.mp4')
#
# body_classifier = cv2.CascadeClassifier('venv/haarcascades/Haarcascades/haarcascade_fullbody.xml')
# w = int(cap.get(3))
# h = int(cap.get(4))
# out = cv2.VideoWriter('walking_output.avi', cv2.VideoWriter_fourcc('M','J','P','G'), 30, (w, h))
#
#
# while(True):
#
#     ret , frame = cap.read()
#     if ret:
#         gray = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
#         bodies = body_classifier.detectMultiScale(gray,1.2,4)
#
#         for (x,y,w,h) in bodies:
#             cv2.rectangle(frame,(x,y),(x+w,y+h),(0,255,0),2)
#
#         out.write(frame)
#     else:
#         break
#
# cap.release()
# out.release()


# for car detection

cap = cv2.VideoCapture('videos/cars.mp4')
car_classifire = cv2.CascadeClassifier('venv/haarcascades/Haarcascades/haarcascade_car.xml')

w = int(cap.get(3))
h = int(cap.get(4))

out = cv2.VideoWriter('Car_output.avi',cv2.VideoWriter_fourcc('M','J','P','G'),30,(w,h))

while(True):
    ret , frame = cap.read()
    if ret:
        gray = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
        cars = car_classifire.detectMultiScale(gray,1.2,4)

        for (x,y,w,h) in cars:
            cv2.rectangle(frame,(x,y),(x+w,y+h),(0,0,255),2)

        out.write(frame)
    else:
         break

cap.release()
out.release()