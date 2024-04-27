from cs1robots import *
load_world('worlds/harvest2.wld')
hubo = Robot()
hubo.set_trace('blue')

def turn_right():
    for i in range(3):
        hubo.turn_left()

def goToStartArea():
    for i in range(5):
        hubo.move()
    hubo.turn_left()
    hubo.move()

def upStair():
    for i in range(5):
        hubo.pick_beeper()
        hubo.move()
        turn_right()
        hubo.move()
        hubo.turn_left()
    hubo.pick_beeper()

def downStair():
    for i in range(5):
        hubo.pick_beeper()
        turn_right()
        hubo.move()
        hubo.turn_left()
        hubo.move()
    hubo.pick_beeper()

def upToDown():
    hubo.move()
    hubo.turn_left()
    hubo.move()
    hubo.turn_left()

def downToUp():
    turn_right()
    hubo.move()
    turn_right()
    hubo.move()

#프로그램 시작
#시작 위치로 이동
goToStartArea()

#up과 down을 반복합니다.
for i in range(2):
    # upStair
    upStair()
    upToDown()

    # downStair
    downStair()
    downToUp()

#마지막 up과 down을 다음과 같이 처리합니다.
upStair()
upToDown()

downStair()