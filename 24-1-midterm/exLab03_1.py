from cs1robots import *
load_world("worlds/beepers1.wld")
hubo = Robot()
hubo.set_trace('blue')
hubo.set_pause(0.3)

while not hubo.on_beeper():
    hubo.move()