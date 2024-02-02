from time import sleep
from e_drone.drone import *
from e_drone.protocol import *

def eventAltitude(altitude):
    print("eventAltitude()")
    print(" - Temperature : ", format(altitude.Temperature))
    print(" - Pressure : ", format(altitude.Pressure))
    print(" - Altitude : ", format(altitude.Altitude))
    print(" - RangeHeight : ", format(altitude.RangeHeight))

if __name__ == "main":
    drone = Drone()
    drone.open("com4")

    drone.setEventHandler(DataType.Altitude, eventAltitude)
    while True:
        drone.sendRequest(DeviceType.Drone, DataType.Altitude)
        eventAltitude(Altitude)
        sleep(1)
