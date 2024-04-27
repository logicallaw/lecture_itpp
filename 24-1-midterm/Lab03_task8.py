from cs1robots import *
load_world("worlds/trash2.wld")
hubo = Robot()
hubo.set_trace('red')

def is_on_beeper():
    while hubo.on_beeper():
        hubo.pick_beeper()

def drop_all_beepers():
    while hubo.carries_beepers():
        hubo.drop_beeper()


def turn_back():
    for i in range(2):
        hubo.turn_left()

def turn_right():
    for i in range(3):
        hubo.turn_left()

#program start
for i in range(9):
    hubo.move()
    is_on_beeper()

turn_back()
for i in range(9):
    hubo.move()
turn_right()
hubo.move()
drop_all_beepers()
