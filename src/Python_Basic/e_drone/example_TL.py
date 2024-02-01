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

    print("Landing")
    drone.sendLanding()
    sleep(3)

    drone.close()
    print("Finish")