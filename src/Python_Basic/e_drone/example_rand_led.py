import random
from time import sleep
from e_drone.drone import *
from e_drone.protocol import *

if __name__ == '__main__':
    drone = Drone(True, True, True, True, True)
    drone.open("com4")
    for i in range(0, 10, 1):           # 0 ~ 10까지 1씩 증가
        r = int(random.randint(0, 255)) # 0 ~ 255의 수를 정수로
        g = int(random.randint(0, 255)) # 0 ~ 255의 수를 정수로
        b = int(random.randint(0, 255)) 
        dataArray = drone.sendLightDefaultColor(LightModeDrone.BodyDimming, 1, r, g, b) # Red
        print(print(f" {i} / {convertByteArrayToString(dataArray)}"))
        sleep(2)
