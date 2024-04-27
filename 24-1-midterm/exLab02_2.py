from cs1robots import *
def move_and_drop():
    hubo.move()
    if not hubo.on_beeper():
        hubo.drop_beeper()

load_world("worlds/beepers1.wld")
hubo = Robot(beepers = 9)
hubo.set_trace("blue")
hubo.set_pause(0.3)

for i in range(9):
    move_and_drop()