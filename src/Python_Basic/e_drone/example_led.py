from time import sleep
from e_drone.drone import *
from e_drone.protocol import *

def exit():
    input_command = input("Press Enter to exit...")
    if input_command == "exit":
        drone.close()
        print("Program Exit")
        return True

if __name__ == '__main__':
    drone = Drone(True, True, True, True, True)
    drone.open("com4")
    while True:
        drone.sendLightDefaultColor(LightModeDrone.BodyDimming, 1, 255, 0, 0) # Red
        sleep(2)
        drone.sendLightDefaultColor(LightModeDrone.BodyDimming, 1, 0, 255, 0) # Green
        sleep(2)
        drone.sendLightDefaultColor(LightModeDrone.BodyDimming, 1, 0, 0, 255) # Blue
        sleep(2)
        if exit() == True:
            break
