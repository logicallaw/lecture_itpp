from cs1robots import *
create_world()
hubo = Robot(orientation = 'W', avenue = 7, street = 5)
hubo.set_trace('blue')

def move_to_wall():
    while hubo.front_is_clear():
        hubo.move()

while not hubo.facing_north():
    hubo.turn_left()

for i in range(2):
    hubo.turn_left()
    move_to_wall()