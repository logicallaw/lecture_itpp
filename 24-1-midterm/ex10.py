from cs1robots import *
create_world()
hubo = Robot()
hubo.turn_left()

def move_to_wall():
    while hubo.front_is_clear():
        hubo.move()

def turn_right():
    for i in range(3):
        hubo.turn_left()

def round():
    move_to_wall()
    turn_right()
    if hubo.right_is_clear():
        hubo.move()
        turn_right()
        move_to_wall()
        hubo.turn_left()
        if hubo.front_is_clear():
            hubo.move()
            hubo.turn_left()

