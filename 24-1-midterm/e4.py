from cs1robots import *
load_world("worlds/harvest4.wld")
hubo = Robot()
hubo.set_trace('blue')
def turn_right():
    for i in range(3):
        hubo.turn_left()

def move_and_pick():
    hubo.move()
    while hubo.on_beeper():
        hubo.pick_beeper()

def move_five():
    for i in range(5):
        move_and_pick()

def harvest_and_pick():
    move_and_pick()
    hubo.turn_left()
    move_five()
    turn_right()
    move_and_pick()
    turn_right()
    move_five()
    hubo.turn_left()
for i in range(3):
    if hubo.front_is_clear():
        harvest_and_pick()
