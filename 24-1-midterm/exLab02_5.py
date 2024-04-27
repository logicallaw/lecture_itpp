from cs1robots import *

def dance():
    for i in range(4):
        hubo.turn_left()

def move_or_turn():
    if hubo.front_is_clear():
        dance()
        hubo.move()
    else:
        hubo.turn_left()
    hubo.drop_beeper()

load_world("worlds/amazing1.wld")
hubo = Robot(beepers=20)
hubo.set_trace("green")
hubo.set_pause(0.3)

for i in range(18):
    move_or_turn()