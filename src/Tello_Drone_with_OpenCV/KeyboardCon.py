from djitellopy import tello
import keyboardModule as km
from time import sleep

km.init()
me = tello.Tello()
me.connect()
print(me.get_battery())

def getKeyboardInput():
    lr, fb, ud, yv = 0, 0, 0, 0
    speed = 50

    if km.getKey("LEFT"): lr = - speed
    elif km.getKey("RIGHT"): lr = speed

    if km.getKey("UP"): fb = speed
    elif km.getKey("DOWN"): fb = -speed

    if km.getKey("w"): ud = speed
    elif km.getKey("s"): ud = -speed

    if km.getKey("a"): yv = speed
    elif km.getKey("d"): yv = -speed

    if km.getKey("q"): me.land()
    if km.getKey("e"): me.takeoff()

    return [lr, fb, ud, yv]

while True:
    vals = getKeyboardInput()
    me.send_rc_control(vals[0], vals[1], vals[2], vals[3])
    sleep(0.05)