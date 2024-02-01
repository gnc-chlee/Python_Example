# Example Code for drone forward movement

from time import sleep
from e_drone.drone import *
from e_drone.protocol import *

if __name__ == "__main__":
    drone = Drone()
    drone.open("com4")
    print("Take Off")
    drone.sendTakeOff()
    altitude = drone.getAltitude()
    print("Altitude:", altitude)
    sleep(1)

    print("Hovering")
    drone.sendControlPosition(0, 0, 0, 0)