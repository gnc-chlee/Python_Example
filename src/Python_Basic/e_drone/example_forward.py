from time import sleep

# BRC-105 모듈 불러오기
from e_drone.drone import *
import e_drone.protocol as protocol

# 메인 실행 부분
if __name__ == '__main__':

    drone1 = Drone()    # 1번째 Drone 객체 생성 후 변수(drone1)에 저장

    # 연결된 각 드론과의 통신을 위한 시리얼 포트 연결 작업
    drone1.open("COM4")    # drone1 시리얼 포트 연결

    # drone LED 점등 붉은색으로 
    drone1.sendLightModeColors(protocol.LightModeDrone.BodyHold, 200, protocol.Colors.Green)
    sleep(1.0)
    
    # 1단계: drone 이륙하기
    print("[Step.1] Drone1 Takeoff")
    drone1.sendTakeOff()    # drone1 이륙
    for i in range(3, 0, -1):   # 이륙하는동안 3초 카운트
        print(i)
        sleep(1.0)

    # 2단계: drone 호버링하기
    print("[Step.2] Drone Hovering")
        # drone LED 점등 깜빡이기
    for i in range(2, 0, -1):   # 2초동안 호버링
        print(i)
        drone1.sendControlWhile(0, 0, 0, 0, 1000)   # drone1 호버링(1초)
        sleep(1.0)

    # 3단계: drone 앞으로 1m 전진하기
    drone1.sendLightModeColors(protocol.LightModeDrone.BodyHold, 200, protocol.Colors.Blue)
    sleep(1.0)
    print("[Step.3] Go Front 1 meter")
    drone1.sendControlPosition(1.0, 0, 0, 0.5, 0, 0)
    for i in range(5, 0, -1):   # 전진하는동안 5초 카운트
        print(i)
        sleep(1.0)

    # 4단계: drone 뒤로 1m 후진하기
    print("[Step.4] Go Back 1 meter")
    drone1.sendControlPosition(-1.0, 0, 0, 0.5, 0, 0)
    for i in range(5, 0, -1):   # 후진하는동안 5초 카운트
        print(i)
        sleep(1.0)

    # 5단계: drone 착륙하기
    print("[Step.5] Drone Landing")
    drone1.sendLightModeColors(protocol.LightModeDrone.BodyHold, 200, protocol.Colors.Red)
    sleep(1.0)
    drone1.sendLanding()    # drone 착륙
    for i in range(5, 0, -1):   # 착륙하는동안 5초 카운트
        print("{0}".format(i))
        sleep(1.0)

    # 시리얼 포트 닫기 작업(모든 명령이 완료되면 시리얼 포트를 닫아줌.)
    drone1.close()  # drone1 시리얼 포트 닫기