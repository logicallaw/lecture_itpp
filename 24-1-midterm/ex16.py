from cs1robots import *
load_world("worlds/harvest2.wld")
hubo = Robot()
def turn_right():
    for i in range(3):
        hubo.turn_left()

def move_five():
    for i in range(5):
        hubo.move()

def harvest_zigzag():
    hubo.pick_beeper()
    hubo.move()
    turn_right()
    hubo.move()
    hubo.turn_left()

def cycle():
    for i in range(5):
        harvest_zigzag()
    hubo.pick_beeper()
    hubo.move()
    hubo.turn_left()
    hubo.move()
    hubo.turn_left()
    for i in range(5):
        harvest_zigzag()
    hubo.pick_beeper()

move_five()
hubo.turn_left()
hubo.move()
for i in range(2):
    cycle()
    turn_right()
    hubo.move()
    turn_right()
    hubo.move()
cycle()