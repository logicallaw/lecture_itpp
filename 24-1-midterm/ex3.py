from cs1robots import *

create_world()
hubo = Robot(beepers=10)
hubo.set_trace("blue")

hubo.drop_beeper()
hubo.move()
hubo.turn_left()
hubo.move()
hubo.drop_beeper()
hubo.pick_beeper()