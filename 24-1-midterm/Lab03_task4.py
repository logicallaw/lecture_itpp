from cs1robots import *
load_world("worlds/harvest4.wld")
hubo = Robot()
hubo.set_trace('blue')

def turn_right():
    for i in range(3):
        hubo.turn_left()

def is_on_beeper():
    while hubo.on_beeper():
        hubo.pick_beeper()

def goStraight():
    for i in range(5):
        is_on_beeper()
        hubo.move()

def turn_left_and_up():
    is_on_beeper()
    hubo.turn_left()
    hubo.move()
    hubo.turn_left()

def turn_right_and_up():
    is_on_beeper()
    turn_right()
    hubo.move()
    turn_right()

#program start
hubo.move()
for i in range(2):
    goStraight()
    turn_left_and_up()
    goStraight()
    turn_right_and_up()

goStraight()
turn_left_and_up()
goStraight()