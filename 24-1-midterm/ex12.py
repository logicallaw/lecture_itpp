from cs1robots import *
load_world("worlds/trash1.wld")
hubo = Robot()
def turn_right():
    for i in range(3):
        hubo.turn_left()

def move_and_pick():
    hubo.move()
    while hubo.on_beeper():
        hubo.pick_beeper()

def turn_around():
    for i in range(2):
        hubo.turn_left()

def pick_litters():
    while hubo.front_is_clear():
        move_and_pick()
    turn_around()

def drop_litters():
    while hubo.front_is_clear():
        hubo.move()
    turn_right()
    hubo.move()
    while hubo.carries_beepers():
        hubo.drop_beeper()

pick_litters()
drop_litters()