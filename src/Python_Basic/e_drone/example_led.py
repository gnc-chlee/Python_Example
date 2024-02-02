from time import sleep
from e_drone.drone import *
from e_drone.protocol import *

def exit():
    input_command = input("Press q and enter to exit...")
    if input_command == "q" or input_command == "Q":
        drone.close()
        print("Program Exit")
        return True

if __name__ == '__main__':
    drone = Drone(True, True, True, True, True)
    drone.open("com4")
    while True:
        user_input = input("Enter a command: ")
        if user_input == True:
            break
        drone.sendLightDefaultColor(LightModeDrone.BodyFlickerDouble, 1, 255, 0, 0) # Red
        sleep(2)
        drone.sendLightDefaultColor(LightModeDrone.BodyDimming, 1, 0, 255, 0) # Green
        sleep(2)
        drone.sendLightDefaultColor(LightModeDrone.BodyDimming, 1, 0, 0, 255) # Blue
        sleep(2)
