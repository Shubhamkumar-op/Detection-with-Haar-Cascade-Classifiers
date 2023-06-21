#working on imgpath
import cv2

face_classifier = cv2.CascadeClassifier('venv/haarcascades/Haarcascades/haarcascade_frontalface_default.xml')
eye_classifier = cv2.CascadeClassifier('venv/haarcascades/Haarcascades/haarcascade_eye.xml')

img = cv2.imread('img/test2.jpg')
gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)


faces = face_classifier.detectMultiScale(gray,1.3,3)
if faces is ():
    print('NO face found')

for (x,y,w,h) in faces:
    cv2.rectangle(img,(x,y),(x+w,y+h),(0,0,255),2)
    roi_gray = gray[y:y+h, x:x+w]
    roi_color = img[y:y+h, x:x+w]
    eyes = eye_classifier.detectMultiScale(roi_gray, 1.2, 3)
    for (ex,ey,ew,eh) in eyes:
        cv2.rectangle(roi_color,(ex,ey),(ex+ew,ey+eh),(255,0,0),2)

# imshow('Eye & Face Detection',img)

# cv2.imshow('Eye & Face Detection',img)
while True:
  cv2.imshow("window",img)
  if cv2.waitKey(1) & 0xFF == ord('x'):
    break

cv2.destroyAllWindows()
