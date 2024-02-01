import time
from e_drone.drone import *
from e_drone.protocol import *


if __name__ == '__main__':
    drone = Drone()
    drone.open("com4")

    State.