from cs1robots import *
create_world()
hubo = Robot(beepers = 1)
hubo.set_trace('blue')


hubo.drop_beeper()
hubo.move()
while not hubo.on_beeper():
    if hubo.front_is_clear():
        hubo.move()
    else:
        hubo.turn_left()
