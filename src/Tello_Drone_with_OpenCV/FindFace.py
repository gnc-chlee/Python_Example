#from djitellopy import tello
import cv2
import numpy as np
import time
#me = tello.Tello()      # create tello object
#me.connect()
#print(me.get_battery()) # print battery state
#me.streamon()
#me.takeoff()
#me.send_rc_control(0, 0, 25, 0)         #updown velocity
#time.sleep(2.2)


w, h = 360, 240
fbRange = [6200, 6800]
pid = [0.4, 0.2, 0]         # P I D
pError = 0

def findFace(img):
    faceCascade = cv2.CascadeClassifier("haarcascade_frontalface_alt.xml")
    imgGray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    faces = faceCascade.detectMultiScale(imgGray, 1.2, 8)

    myFaceListC = []        # Center
    myFaceListArea = []

    for (x, y, w, h) in faces:
        cv2.rectangle(img, (x, y), (x+w, y+h), (0, 0, 255), 2)
        cx = x + w //2
        cy = y + h //2
        area = w * h
        cv2.circle(img, (cx, cy), 5, (0, 255, 0), cv2.FILLED)
        myFaceListC.append([cx, cy])
        myFaceListArea.append(area)

    if len(myFaceListArea) != 0:
        i = myFaceListArea.index(max(myFaceListArea))
        return img, [myFaceListC[i], myFaceListArea[i]]
    else:
        return img, [[0, 0], 0]

def trackFace(info, w, pid, pError):
    area = info[1]
    x, y = info[0]
    fb = 0
    error = x - w//2
    speed = pid[0] * error + pid[1] * (error - pError)
    speed = int(np.clip(speed, -100, 100))

    area = info[1]
    if area > fbRange[0] and area <fbRange[1]:      # Green Zone
        fb = 0
    elif area > fbRange[1]:                         # Move backward
        fb = -20
    elif area < fbRange[0] and area != 0:           # Move Forward
        fb = 20

    if x == 0:
        speed = 0
        error = 0
    print(speed, fb)

    #me.send_rc_control(0, fb, 0, speed)
    return error

cap = cv2.VideoCapture(0)       # using wepcam num 0


while True:
    _, img = cap.read()
    #img = me.get_frame_read().frame
    img = cv2.resize(img, (w, h))
    img, info = findFace(img)
    pError - trackFace(info, w, pid, pError)
    print("Center", info[0], "Area", info[1])
    cv2.imshow("Output", img)
    cv2.waitKey(1)

