from cs1robots import *
load_world("worlds/harvest4.wld")
hubo = Robot()
hubo.set_trace('blue')
hubo.set_pause(0.3)


hubo.move()
def pick_and_move():
    while hubo.on_beeper():
        hubo.pick_beeper()
    hubo.move()

pick_and_move()
