from cs1robots import *

load_world('worlds/newspaper.wld')
hubo = Robot(beepers=1)
hubo.set_trace('blue')

def turn_right():
    for i in range(3):
        hubo.turn_left()

def turn_back():
    for i in range(2):
        hubo.turn_left()

def upStair():
    hubo.turn_left()
    hubo.move()
    turn_right()
    hubo.move()

def downStair():
    hubo.move()
    hubo.turn_left()
    hubo.move()
    turn_right()


for i in range(4):
    hubo.move()
    upStair()
hubo.move()
hubo.drop_beeper()
turn_back()

for i in range(4):
    hubo.move()
    downStair()
hubo.move()
