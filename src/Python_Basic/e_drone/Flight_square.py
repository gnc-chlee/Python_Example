from time import sleep

# BRC-105 모듈 불러오기
from e_drone.drone import *
from e_drone.protocol import *

# 메인 실행 부분
if __name__ == '__main__':

    drone1 = Drone()    # 1번째 Drone 객체 생성 후 변수(drone1)에 저장
    drone2 = Drone()    # 2번째 Drone 객체 생성 후 변수(drone2)에 저장

    # 연결된 각 드론과의 통신을 위한 시리얼 포트 연결 작업
    drone1.open("COM5")    # drone1 시리얼 포트 연결
    drone2.open("COM8")    # drone2 시리얼 포트 연결

    # 1단계: drone1/2 이륙하기
    print("[Step.1] Drone1/2 Takeoff")
    drone1.sendTakeOff()    # drone1 이륙
    sleep(0.1)
    drone2.sendTakeOff()    # drone2 이륙
    for i in range(0, 5, 1):   # 이륙하는동안 5초 카운트
        print(i)
        sleep(1)
    
    # drone1/2 LED 점등
    drone1.sendLightModeColors(LightModeDrone.BodyHold, 200, Colors.RosyBrown)
    sleep(0.1)
    drone2.sendLightModeColors(LightModeDrone.BodyHold, 200, Colors.Yellow)
    sleep(1.0)

    # 2단계: drone1/2 호버링하기
    print("[Step.2] Drone1/2 Hovering")
    for i in range(0, 2, 1):   # 2초동안 호버링
        print(i)
        drone1.sendControlWhile(0, 0, 0, 0, 1000)   # drone1 호버링(1초)
        sleep(0.1)
        drone2.sendControlWhile(0, 0, 0, 0, 1000)   # drone2 호버링(1초)
        sleep(1)

    # 3단계: drone1 전진
    print("[Step.3] Go")
    drone1.sendControlPosition(0.5, 0.0, 0.0, 0.5, 0, 0)    # drone1 0.5m/s 속도로 0.5m 전진
    sleep(0.1)
    drone2.sendControlPosition(0.0, 0.0, 0.5, 0.5, 0, 0)    # drone2 0.5m/s 속도로 0.5m 상승
    for i in range(0, 3, 1):   # 3초 카운트
        print(i)
        sleep(1)

    print("Drone1/2 Hovering")
    for i in range(0, 1, 1):   # 1초동안 호버링
        print(i)
        drone1.sendControlWhile(0, 0, 0, 0, 1000)   # drone1 호버링(1초)
        sleep(0.1)
        drone2.sendControlWhile(0, 0, 0, 0, 1000)   # drone2 호버링(1초)
        sleep(1)

    # 4단계: drone1 우측 drone2 좌측
    print("[Step.4] Go")
    drone1.sendControlPosition(0.0, -0.5, 0.0, 0.5, 0, 0)    # drone1 0.5m/s 속도로 1.0m 전진
    sleep(0.1)
    drone2.sendControlPosition(0.0, 0.5, 0.0, 0.5, 0, 0)    # drone2 0.5m/s 속도로 1.0m 전진
    for i in range(0, 3, 1):   # 3초 카운트
        print(i)
        sleep(1)

    print("Drone1/2 Hovering")
    for i in range(0, 1, 1):   # 1초동안 호버링
        print(i)
        drone1.sendControlWhile(0, 0, 0, 0, 1000)   # drone1 호버링(1초)
        sleep(0.1)
        drone2.sendControlWhile(0, 0, 0, 0, 1000)   # drone2 호버링(1초)
        sleep(1)

    # 5단계: drone1 후진 drone2 전진
    print("[Step.5] Go 2")
    drone1.sendControlPosition(-0.5, 0.0, 0.0, 0.5, 0, 0)    # drone1 0.5m/s 속도로 1.0m 전진
    sleep(0.1)
    drone2.sendControlPosition(0.5, 0.0, 0.0, 0.5, 0, 0)    # drone2 0.5m/s 속도로 1.0m 전진
    for i in range(0, 3, 1):   # 이동하는동안 3초 카운트
        print(i)
        sleep(1)

    print("Drone1/2 Hovering")
    for i in range(0, 1, 1):   # 1초동안 호버링
        print(i)
        drone1.sendControlWhile(0, 0, 0, 0, 1000)   # drone1 호버링(1초)
        sleep(0.1)
        drone2.sendControlWhile(0, 0, 0, 0, 1000)   # drone2 호버링(1초)
        sleep(1)

    # 6단계: drone1 좌측 drone2 우측
    print("[Step.6] Go")
    drone1.sendControlPosition(0.0, 0.5, 0.0, 0.5, 0, 0)    # drone1 0.5m/s 속도로 1.0m 전진
    sleep(0.1)
    drone2.sendControlPosition(0.0, -0.5, 0.0, 0.5, 0, 0)    # drone2 0.5m/s 속도로 1.0m 전진
    for i in range(0, 3, 1):   # 이동하는동안 3초 카운트
        print(i)
        sleep(1)

    print("Drone1/2 Hovering")
    for i in range(0, 1, 1):   # 1초동안 호버링
        print(i)
        drone1.sendControlWhile(0, 0, 0, 0, 1000)   # drone1 호버링(1초)
        sleep(0.1)
        drone2.sendControlWhile(0, 0, 0, 0, 1000)   # drone2 호버링(1초)
        sleep(1)

    # 7단계: drone2 후진
    print("[Step.7] Go")
    drone2.sendControlPosition(-0.5, 0.0, 0.0, 0.5, 0, 0)    # drone2 0.5m/s 속도로 1.0m 전진
    for i in range(0, 3, 1):   # 이동하는동안 5초 카운트
        print(i)
        sleep(1)

    print("Drone1/2 Hovering")
    for i in range(0, 1, 1):   # 1초동안 호버링
        print(i)
        drone1.sendControlWhile(0, 0, 0, 0, 1000)   # drone1 호버링(1초)
        sleep(0.1)
        drone2.sendControlWhile(0, 0, 0, 0, 1000)   # drone2 호버링(1초)
        sleep(1)

    # 8단계: drone1/2 착륙하기
    print("[Step.8] Drone1/2 Landing")
    drone1.sendLanding()    # drone1 착륙
    sleep(0.1)
    drone2.sendLanding()    # drone2 착륙
    for i in range(0, 5, 1):   # 착륙하는동안 5초 카운트
        print(i)
        sleep(1)

    # 시리얼 포트 닫기 작업(모든 명령이 완료되면 시리얼 포트를 닫아줌.)
    drone1.close()  # drone1 시리얼 포트 닫기
    drone2.close()  # drone2 시리얼 포트 닫기