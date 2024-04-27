from cs1robots import *
def turn_right():
    for i in range(3):
        hubo.turn_left()
load_world("worlds/amazing3.wld")
hubo = Robot(beepers = 1)
hubo.set_trace('blue')


hubo.drop_beeper()
if not hubo.front_is_clear():
    hubo.turn_left()
hubo.move()
while not hubo.on_beeper():
    if hubo.right_is_clear():
        turn_right()
        hubo.move()
    if hubo.front_is_clear():
        hubo.move()
    else:
        hubo.turn_left()
