from cs1robots import *
load_world('worlds/harvest2.wld')
hubo = Robot()
hubo.set_trace('blue')

def turn_right():
    for i in range(3):
        hubo.turn_left()
def set_start_point():
    for i in range(5):
        hubo.move()
    hubo.turn_left()
    hubo.move()
def is_on_beeper():
    while hubo.on_beeper():
        hubo.pick_beeper()
def upBridge():
    is_on_beeper()
    hubo.move()
    hubo.turn_left()
    hubo.move()

def downBridge():
    is_on_beeper()
    hubo.move()
    turn_right()
    hubo.move()
def goUp():
    is_on_beeper()
    hubo.move()
    turn_right()
    hubo.move()
    hubo.turn_left()
def goDown():
    is_on_beeper()
    hubo.move()
    hubo.turn_left()
    hubo.move()
    turn_right()

def one_cycle():
    for i in range(5):
        goUp()
    upBridge()
    for i in range(5):
        goDown()
    downBridge()

#program start
set_start_point()
for i in range(2):
    one_cycle()

for i in range(5):
    goUp()
upBridge()
for i in range(5):
    goDown()
is_on_beeper()



