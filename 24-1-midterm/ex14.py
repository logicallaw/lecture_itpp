from cs1robots import *
load_world("worlds/harvest1.wld")
hubo = Robot()
def move_and_pick():
    hubo.move()
    while hubo.on_beeper():
        hubo.pick_beeper()

def turn_right():
    for i in range(3):
        hubo.turn_left()

def move_fives():
    for i in range(5):
        move_and_pick()

def harvest_zigzag():
    move_and_pick()
    hubo.turn_left()
    move_fives()
    turn_right()
    move_and_pick()
    turn_right()
    move_fives()
    hubo.turn_left()

for i in range(3):
    harvest_zigzag()