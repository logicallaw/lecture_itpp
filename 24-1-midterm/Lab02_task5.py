from cs1robots import *
load_world('worlds/harvest3.wld')
hubo = Robot(beepers = 20)
hubo.set_trace('blue')

def turn_right():
    for i in range(3):
        hubo.turn_left()

def goStraight():
    for i in range(5):
        if not hubo.on_beeper():
            hubo.drop_beeper()
        hubo.move()

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

if not hubo.on_beeper():
    hubo.drop_beeper()
goLeft()
goStraight()
if not hubo.on_beeper():
    hubo.drop_beeper()