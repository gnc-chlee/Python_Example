# Example code for e_drone
# when drone takes off and lands

from time import sleep
from e_drone.drone import *
from e_drone.protocol import *

if __name__ == '__main__':
    drone = Drone()
    drone.open("com4")

    print("TakeOff")
    drone.sendTakeOff()
    sleep(3)

    print("Moving forward")
    drone.sendControlPosition(2,0,0,0.5,0,0)
    sleep(10)

    print("Moving up")
    drone.sendControlPosition(0,0,0.5,0.5,0,0)
    sleep(5)

    print("Landing")
    drone.sendLanding()
    sleep(3)

    drone.close()
    print("Finish")

    # drone.sendControlPosition(0, 0, 0, 0, 0, 0)  # xpos, ypos, zpos, velocity heading rot_vel
    # drone.sendControlWhile(0, 0, 0, 0, 1000)  # roll, pitch, yaw, zpos, time[ms]