from cs1robots import *
create_world(avenues=10, streets=7) #가로:avenuse, 세로:streets
hubo = Robot()
hubo.set_trace('blue')

hubo.turn_left()

def turn_right():
    for i in range(3):
        hubo.turn_left()

def go():
    while not hubo.front_is_clear():
        hubo.move()
    if (hubo.right_is_clear()):
        turn_right()
        hubo.move()
        turn_right()


hubo.turn_left()