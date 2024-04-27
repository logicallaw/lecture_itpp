from cs1robots import *
load_world('worlds/harvest1.wld')
hubo = Robot()
hubo.set_trace('blue')

def turn_right():
    for i in range(3):
        hubo.turn_left()

def goStraight():
    hubo.pick_beeper()
    for i in range(5):
        hubo.move()
        hubo.pick_beeper()

def goLeft():
    hubo.turn_left()
    hubo.move()
    hubo.turn_left()

def goRight():
    turn_right()
    hubo.move()
    turn_right()

#프로그램 시작
hubo.move()
goStraight()
for i in range(2):
    goLeft()
    goStraight()
    goRight()
    goStraight()

goLeft()
goStraight()