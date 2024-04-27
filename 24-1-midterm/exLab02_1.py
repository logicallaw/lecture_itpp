from cs1robots import *

def turn_right():
    for i in range(3):
        hubo.turn_left()
def move_and_pick():
    hubo.move()
    if hubo.on_beeper():
        hubo.pick_beeper()

load_world("worlds/beepers1.wld")
hubo = Robot()
hubo.set_trace('blue')
hubo.set_pause(0.3)

for i in range(9):
    move_and_pick()