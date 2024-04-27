from cs1robots import *

create_world()
hubo = Robot()
hubo.set_trace('blue')

def turn_right():
    for i in range(3):
        hubo.turn_left()

def turn_left():
    hubo.turn_left()

def move():
    for i in range(9):
        hubo.move()

def up():
    move()
    turn_right()
    hubo.move()
    turn_right()

def down():
    move()
    turn_left()
    hubo.move()
    turn_left()

def zigzag():
    turn_left()
    for i in range(4):
        up()
        down()
    up()
    move()

zigzag()