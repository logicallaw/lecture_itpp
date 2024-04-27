from cs1robots import *

def move_or_turn():
    if hubo.front_is_clear():
        hubo.move()
    else:
        hubo.turn_left()

load_world("worlds/amazing1.wld")
hubo = Robot(beepers = 10)
hubo.set_trace("green")
hubo.set_pause(0.3)

for i in range(20):
    move_or_turn()
