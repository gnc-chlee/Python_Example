from time import sleep

from e_drone.drone import *
from e_drone.protocol import *
import keyboard



if __name__ == '__main__':

    drone = Drone()
    drone.open()
    count = 0
    while 1:
        if keyboard.is_pressed("1"):
            print("TakeOff")
            drone.sendTakeOff()
            sleep(0.5)
            drone.sendControlWhile(0,0,0,0,4000)
            
        elif keyboard.is_pressed("2"):
            print("Landing")
            drone.sendLanding()
            sleep(0.5)
        
        if keyboard.is_pressed("w") or keyboard.is_pressed("W"):
            print("Go Front")
            drone.sendControl(0, 20, 0, 0)
            sleep(0.1)
        elif keyboard.is_pressed("s") or keyboard.is_pressed("S"):
            print("Go Back")
            drone.sendControl(0, -20, 0, 0)
            sleep(0.1)

        if keyboard.is_pressed("a") or keyboard.is_pressed("A"):
            print("Go Left")
            drone.sendControl(-20, 0, 0, 0)
            sleep(0.1)
        elif keyboard.is_pressed("d") or keyboard.is_pressed("D"):
            print("Go Right")
            drone.sendControl(20, 0, 0, 0)
            sleep(0.1)

        if keyboard.is_pressed("z") or keyboard.is_pressed("Z"):
            print("Go Up")
            drone.sendControl(0, 0, 0, 20)
            sleep(0.1)
        elif keyboard.is_pressed("c") or keyboard.is_pressed("C"):
            print("Go Down")
            drone.sendControl(0, 0, 0, -20)
            sleep(0.1)

        if keyboard.is_pressed("Space"):
            print("Stop")
            drone.sendControl(0, 0, 0, 0)
            sleep(0.1)
        
    drone.close()