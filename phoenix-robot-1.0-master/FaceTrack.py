import numpy as np
import os
#import RPi.GPIO as GPLIO
import sys
sys.path.append('/usr/local/lib/python3.5/site-packages')
import angleServoCtrl
import cv2
panPin = 0
tiltPin = 0


face_cascade = cv2.CascadeClassifier('/home/pi/Downloads/Raspi2/haarcascade_frontalface_default.xml')

eye_cascade = cv2.CascadeClassifier('/home/pi/Downloads/Raspi2/haarcascade_eye.xml')

cap = cv2.VideoCapture(0)
cap.set(3, 480) # set Width
cap.set(4, 640) # set Height


print(cap.read())
##global panServoAngle
##panServoAngle = 90
##
##global tiltServoAngle
##tlitServoAngle = 105
##
##print ("positioning Servos to intial stage")
##os.system("python angleServoCtrl.py" + str(panPin) + " " + str(panServoAngle))
##os.system("python3 angleServoCtrl.py" + str(tiltPin) + " " + str(panServoAngle))
##
##
##def servo_position_center(x,y):
##    global panServoAngle
##    global tiltServoAngle
##
##    if(x < 250):
##        panServoAngle += 10
##        if panServoAngle > 140:
##            #servo can not exceed 140 degree
##            panServoAngle = 140
##        os.system("python angleServoCtrl.py " + str(panPin) + " "  + str(panServoAngle))
##
##    if (x > 300):
##        panServoAngle -= 10
##        if panServoAngle < 40:
##            panServoAngle = 40
##        os.system("python angleServoCtrl.py " + str(panPin) + " "  + str(panServoAngle))
##
##    if(y < 160):
##        tiltServoAngle += 10
##        if tiltServoAngle > 140:
##            tiltServoAngle = 140
##        os.system("python angleServoCtrl.py " + str(tiltPin) + " " + str(tiltServoAngle))
##
##    if(y > 210):
##        tiltServoAngle -= 10
##        if tiltServoAngle < 40:
##            tiltServoAngle = 40
##        os.system("python angleServoCtrl.py " + str(tiltPin) + " " + str(tiltServoAngle))
##
##


while True:
    ret, frame = cap.read()
    #frame = cv2.flip(frame, -1)
    #frame = np.full((800,800,4), 12, dtype = np.uint8)
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(frame, 1.3, 5)
    
    for (x,y,w,h) in faces:
        cv2.rectangle(frame,(x,y),(x+w,y+h),(255,0,0),2)
        roi_gray = frame[y:y+h, x:x+w]
        roi_color = gray[y:y+h, x:x+w]
        print(x)
        eyes = eye_cascade.detectMultiScale(roi_gray)
        for (ex,ey,ew,eh) in eyes:
            cv2.rectangle(roi_color,(ex,ey),(ex+ew,ey+eh),(0,255,0),2)

    cv2.imshow('frame',gray)
    k = cv2.waitKey(15) & 0xff
    if k == 27:         # wait for ESC key to exit
        break

cap.release()
cv2.destroyAllWindows()

    
            
