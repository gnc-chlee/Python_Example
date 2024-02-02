from time import sleep
from e_drone.drone import *
from e_drone.protocol import *

def eventMotion(motion):
    print("print motion")
    print(" Accel : ", format(motion.accelX, motion.accelY, motion.accelZ))
    print(" Gyro : ", format(motion.gyroX, motion.gyroY, motion.gyroZ))
    print(" Angle : ", format(motion.angleRoll, motion.anglePitch, motion.angleYaw))

if __name__ == "__main__":
    drone = Drone()
    drone.open("com4")

    drone.setEventHandler(DataType.Motion, eventMotion)

    sleep(0.01)

    drone.sendRequest(DeviceType.Drone, DataType.Motion)
    sleep(0.01)

    drone.close()