from cs1robots import *
load_world("worlds/hurdles2.wld")
hubo = Robot()
hubo.set_trace('blue')
def turn_right():
    for i in range(3):
        hubo.turn_left()
def jump_one_hurdle():
    hubo.turn_left()
    hubo.move()
    turn_right()
    hubo.move()
    hubo.move()
    turn_right()
    hubo.move()
    hubo.turn_left()
