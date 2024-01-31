from djitellopy import tello
import cv2
me = tello.Tello()              # create tello object
me.connect()
print(me.get_battery())        # print battery state

me.streamon()

while True:
    img = me.get_frame_read().frame
    img = cv2.resize(img,(360,240))     # image small it can be get faster
    cv2.imshow("Image", img)
    cv2.waitKey(1)
