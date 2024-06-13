from cs1robots import *
hubo_direction = 0
hubo = Robot()
def turn_left():
    hubo.turn_left()
    global hubo_direction
    hubo_direction += 90

def turn_right():
    for i in range(3):
        hubo.turn_left()
    global hubo_direction
    hubo_direction -= 90

