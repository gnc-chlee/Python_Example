from time import sleep
from e_drone.drone import *
from e_drone.protocol import *

def user_input():
    user_input = input("Enter a command: ")
    if user_input == "q":
        return True

if __name__ == '__main__':
    drone = Drone(True, True, True, True, True)
    drone.open("com4")
    while True:
        if user_input():
            break
        drone.sendLightDefaultColor(LightModeDrone.BodyFlickerDouble, 1, 255, 0, 0) # Red
        sleep(2)
        drone.sendLightDefaultColor(LightModeDrone.BodyDimming, 1, 0, 255, 0) # Green
        sleep(2)
        drone.sendLightDefaultColor(LightModeDrone.BodyDimming, 1, 0, 0, 255) # Blue
        sleep(2)
