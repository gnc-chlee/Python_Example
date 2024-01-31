from djitellopy import tello
import time

me = tello.Tello()      # create tello object
me.connect()            # connect tello

while True:
    print('battery', me.get_battery()) # print battery state
    print('Accel:', me.get_acceleration_x(), me.get_acceleration_y(), me.get_acceleration_z())
    print('baro', me.get_barometer())
    time.sleep(1)                      # Unit : secs