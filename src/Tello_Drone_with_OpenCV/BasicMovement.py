from djitellopy import tello
from time import sleep

me = tello.Tello()      # create tello object
me.connect()
print(me.get_battery()) # print battery state