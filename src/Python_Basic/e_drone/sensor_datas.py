from time import sleep

from e_drone.drone import *
from e_drone.protocol import *

altitude_data = 0
range_data = 0

def eventMotion(motion):
    print("eventMotion()")
    print("- Accel: {0:5}, {1:5}, {2:5}".format(motion.accelX, motion.accelY, motion.accelZ))
    print("-  Gyro: {0:5}, {1:5}, {2:5}".format(motion.gyroRoll, motion.gyroPitch, motion.gyroYaw))
    print("- Angle: {0:5}, {1:5}, {2:5}".format(motion.angleRoll, motion.anglePitch, motion.angleYaw))

def eventAltitude(altitude):
    # print("eventAltitude()")
    # print("-  Temperature: {0:.3f}".format(altitude.temperature))
    # print("-     Pressure: {0:.3f}".format(altitude.pressure))
    # print("-     Altitude: {0:.3f}".format(altitude.altitude))
    altitude_data = altitude.altitude



def eventRange(range):
    # print("eventRange()")
    # print("- RangeFront: {0:.3f}".format(range.front))
    range_value = range.front
    formatted_range = "{:.3f}".format(range_value)
    range_data = float(formatted_range)
    # print("- RangeFront as string: {}".format(range_data))
    print(range.front)

    


if __name__ == '__main__':

    drone = Drone()
    drone.open()
    count = 0
    while 1:
        count += 1
        if count > 1000:
            # 이벤트 핸들링 함수 등록
            # drone.setEventHandler(DataType.Motion, eventMotion)

            # motion 정보 요청
            # drone.sendRequest(DeviceType.Drone, DataType.Motion)
            sleep(0.1)

            # 이벤트 핸들링 함수 등록
            drone.setEventHandler(DataType.Altitude, eventAltitude)
            sleep(0.1)

            # Altitude 정보 요청
            drone.sendRequest(DeviceType.Drone, DataType.Altitude)
            sleep(0.1)
            print(altitude_data)
            # # 이벤트 핸들링 함수 등록
            # drone.setEventHandler(DataType.Range, eventRange)

            get_range = drone.getData(DataType.Range)
            # print(get_range)
            # Range 정보 요청
            drone.sendRequest(DeviceType.Drone, DataType.Range)

            # print(range_data)

            count = 0

    drone.close()