from djitellopy import tello
import cv2
import numpy as np

me = tello.Tello()              # create tello object
me.connect()
print(me.get_battery())        # print battery state
me.streamon()
me.takeoff()

cap = cv2.VideoCapture(0)
hsvVals = [0, 0, 255, 179, 255, 255]
sensors = 3
width, height = 480, 360
threshold = 0.2                     # 20 Percent

sensitivity = 3     # if number is high less sensitive

weights = [-25, -15, 0, 15, 25]
fSpeed = 15
curve = 0

def thresholding(img):
    hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)  # Huge Saturation Value
    lower = np.array([hsvVals[0], hsvVals[1], hsvVals[2]])
    upper = np.array([hsvVals[3], hsvVals[4], hsvVals[5]])
    mask = cv2.inRange(hsv, lower, upper)
    return mask


def getContours(imgThres, img):
    cx = 0
    contours, hieracrhy = cv2.findContours(imgThres, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)
    if len(contours) != 0:
        biggest = max(contours, key=cv2.contourArea)
        x, y, w, h = cv2.boundingRect(biggest)
        cx = x + w // 2  # Center of X
        cy = y + h // 2  # Center of Y
        cv2.drawContours(img, biggest, -1, (255, 0, 255),7)  # only draw biggest one , if you contours, you have draw many white area
        cv2.circle(img, (cx, cy), 10, (0, 255, 0), cv2.FILLED)

    return cx


# Idea is that we want to split our image into three different portion(section)
# these are matrix, we can use the numpy library to actually split it
# very good function that, the width of image should be divisible by three

def getSensorOutput(imgThres, sensors):
    imgs = np.hsplit(imgThres, sensors)
    totalPixels = (img.shape[1] // sensors) * img.shape[0]
    senOut = []

    # it will divided by three then, it will give us the width our single image
    # multiplying the width by height and that it will give us total number of pixels
    for x, im in enumerate(imgs):
        pixelCount = cv2.countNonZero(im)  # to do for counting write here
        if pixelCount > threshold * totalPixels:
            senOut.append(1)
        else:
            senOut.append(0)

        #cv2.imshow(str(x), im)              # we want to show image , later remove this

    print(senOut)
    return senOut
    # when line is very big, it unable to find the biggest conture, it will be error

def sendCommands(senOut, cx):
    global curve
    ## TRANSLATION
    lr = (cx - width//2)//sensitivity
    lr = int(np.clip(lr, -10, 10))      # saturation
    if lr < 2 and lr > -2: lr = 0

    ## Rotation
    if   senOut == [1, 0, 0]: curve = weights[0]
    elif senOut == [1, 1, 0]: curve = weights[1]
    elif senOut == [0, 1, 0]: curve = weights[2]
    elif senOut == [0, 1, 1]: curve = weights[3]
    elif senOut == [0, 0, 1]: curve = weights[4]

    elif senOut == [0, 0, 0]: curve = weights[2]
    elif senOut == [1, 1, 1]: curve = weights[2]
    elif senOut == [1, 0, 1]: curve = weights[2]

    me.send_rc_control(lr, fSpeed, 0, curve)


while True:
    #_, img = cap.read()
    img = me.get_frame_read().frame
    img = cv2.resize(img, (width, height))
    img = cv2.flip(img, 0)              # verticle

    imgThres = thresholding(img)
    cx = getContours(imgThres, img)  # For translation
    senOut = getSensorOutput(imgThres, sensors) ## For Rotation
    sendCommands(senOut, cx)
    cv2.imshow("Output", img)
    cv2.imshow("Path", imgThres)
    cv2.waitKey(1)
