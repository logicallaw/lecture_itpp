from cs1robots import  *
create_world()
hubo = Robot()
hubo.set_trace('blue')

#turn_right() 함수는 default로 생각하고 항상 작성하고 가자.
def turn_right():
    for i in range(3):
        hubo.turn_left()

hubo.move()
hubo.turn_left()
hubo.move()
turn_right()