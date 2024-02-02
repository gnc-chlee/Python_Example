from time import sleep

# BRC-105 모듈 불러오기
from e_drone.drone import *
from e_drone.protocol import *

# 메인 실행 부분
if __name__ == '__main__':

    drone1 = Drone()    # 1번째 Drone 객체 생성 후 변수(drone1)에 저장

    # 연결된 각 드론과의 통신을 위한 시리얼 포트 연결 작업
    drone1.open("COM5")    # drone1 시리얼 포트 연결

    # drone LED 점등 붉은색으로 
    drone1.sendLightDefaultColor(LightModeDrone.BodyDimming, 200, 200, 0, 0)
    sleep(1.0)

    # 시작 전 버저 소리를 없앰
    drone1.sendBuzzer(BuzzerMode.Mute, BuzzerScale.Mute.value, 100)
    sleep(0.2)

    # Handclap 후렴구 부분
    # for문을 통해 3번 반복
    for i in range(3):

        drone1.sendBuzzerScale(BuzzerScale.DS5, 150)
        sleep(0.2)
        drone1.sendBuzzerScale(BuzzerScale.F5, 150)
        sleep(0.2)
        drone1.sendBuzzerScale(BuzzerScale.G5, 150)
        sleep(0.2)
        drone1.sendBuzzerScale(BuzzerScale.G5, 550)
        sleep(0.6)
        drone1.sendBuzzerScale(BuzzerScale.F5, 150)
        sleep(0.2)
        drone1.sendBuzzerScale(BuzzerScale.DS5, 150)
        sleep(0.2)
        drone1.sendBuzzerScale(BuzzerScale.DS5, 350)
        sleep(0.4)
        drone1.sendBuzzerScale(BuzzerScale.GS4, 150)
        sleep(0.2)
        drone1.sendBuzzerScale(BuzzerScale.F5, 600)
        sleep(1.0)

        drone1.sendBuzzerScale(BuzzerScale.DS5, 150)
        sleep(0.2)
        drone1.sendBuzzerScale(BuzzerScale.F5, 150)
        sleep(0.2)
        drone1.sendBuzzerScale(BuzzerScale.G5, 150)
        sleep(0.2)
        drone1.sendBuzzerScale(BuzzerScale.G5, 550)
        sleep(0.6)
        drone1.sendBuzzerScale(BuzzerScale.F5, 150)
        sleep(0.2)
        drone1.sendBuzzerScale(BuzzerScale.DS5, 150)
        sleep(0.2)
        drone1.sendBuzzerScale(BuzzerScale.F5, 350)
        sleep(0.4)
        drone1.sendBuzzerScale(BuzzerScale.G5, 350)
        sleep(0.4)
        drone1.sendBuzzerScale(BuzzerScale.DS5, 150)
        sleep(0.2)
        drone1.sendBuzzerScale(BuzzerScale.C5, 350)
        sleep(0.6)


    drone1.sendBuzzerScale(BuzzerScale.DS5, 150)
    sleep(0.2)
    drone1.sendBuzzerScale(BuzzerScale.F5, 150)
    sleep(0.2)
    drone1.sendBuzzerScale(BuzzerScale.G5, 150)
    sleep(0.2)
    drone1.sendBuzzerScale(BuzzerScale.G5, 350)
    sleep(0.4)
    drone1.sendBuzzerScale(BuzzerScale.G5, 150)
    sleep(0.2)
    drone1.sendBuzzerScale(BuzzerScale.G5, 350)
    sleep(0.4)
    drone1.sendBuzzerScale(BuzzerScale.AS5, 150)
    sleep(0.2)
    drone1.sendBuzzerScale(BuzzerScale.G5, 150)
    sleep(0.2)
    drone1.sendBuzzerScale(BuzzerScale.F5, 150)
    sleep(0.2)
    drone1.sendBuzzerScale(BuzzerScale.G5, 150)
    sleep(0.2)
    drone1.sendBuzzerScale(BuzzerScale.F5, 300)
    sleep(0.35)
    drone1.sendBuzzerScale(BuzzerScale.DS5, 50)
    sleep(0.05)
    drone1.sendBuzzerScale(BuzzerScale.C5, 200)
    sleep(0.95)

    drone1.sendBuzzerScale(BuzzerScale.AS4, 200)
    sleep(0.2)
    drone1.sendBuzzerScale(BuzzerScale.C5, 150)
    sleep(0.2)
    drone1.sendBuzzerScale(BuzzerScale.C5, 150)
    sleep(0.2)
    drone1.sendBuzzerScale(BuzzerScale.C5, 150)
    sleep(0.2)
    drone1.sendBuzzerScale(BuzzerScale.C5, 150)
    sleep(0.2)
    drone1.sendBuzzerScale(BuzzerScale.DS5, 350)
    sleep(0.4)
    drone1.sendBuzzerScale(BuzzerScale.C5, 350)
    sleep(0.4)

    # 전구우우우욱
    drone1.sendBuzzerScale(BuzzerScale.G5, 150)
    sleep(0.2)
    drone1.sendBuzzerScale(BuzzerScale.G5, 550)
    sleep(0.6)

    drone1.sendBuzzerScale(BuzzerScale.G5, 150)
    sleep(0.2)
    drone1.sendBuzzerScale(BuzzerScale.F5, 150)
    sleep(0.2)
    drone1.sendBuzzerScale(BuzzerScale.DS5, 150)
    sleep(0.2)
    drone1.sendBuzzerScale(BuzzerScale.F5, 150)
    sleep(0.2)
    drone1.sendBuzzerScale(BuzzerScale.G5, 350)
    sleep(0.4)
    drone1.sendBuzzerScale(BuzzerScale.GS5, 150)
    sleep(0.2)
    drone1.sendBuzzerScale(BuzzerScale.AS5, 350)
    sleep(0.4)
    drone1.sendBuzzerScale(BuzzerScale.C6, 350)
    sleep(0.4)
    drone1.sendBuzzerScale(BuzzerScale.G5, 150)
    sleep(0.2)
    drone1.sendBuzzerScale(BuzzerScale.AS5, 550)
    sleep(0.6)
    drone1.sendBuzzerScale(BuzzerScale.DS5, 1150)
    sleep(1.3)

    for i in range(2):
        drone1.sendBuzzerScale(BuzzerScale.DS6, 50)
        sleep(0.1)
    drone1.sendBuzzerScale(BuzzerScale.DS6, 150)
    sleep(0.2)
    for i in range(2):
        drone1.sendBuzzerScale(BuzzerScale.D6, 50)
        sleep(0.1)
    drone1.sendBuzzerScale(BuzzerScale.D6, 150)
    sleep(0.2)
    for i in range(2):
        drone1.sendBuzzerScale(BuzzerScale.C6, 50)
        sleep(0.1)
    drone1.sendBuzzerScale(BuzzerScale.C6, 150)
    sleep(0.2)
    drone1.sendBuzzerScale(BuzzerScale.G5, 150)
    sleep(0.2)
    drone1.sendBuzzerScale(BuzzerScale.AS5, 550)
    sleep(0.6)
    drone1.sendBuzzerScale(BuzzerScale.GS5, 950)
    sleep(1.2)


    # 시리얼 포트 닫기 작업(모든 명령이 완료되면 시리얼 포트를 닫아줌.)
    drone1.close()  # drone1 시리얼 포트 닫기