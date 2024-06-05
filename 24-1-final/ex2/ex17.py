from cs1robots import *
load_world("../worlds/add1.wld")
hubo = Robot(street = 2)
def turn_right():
    for i in range(3):
        hubo.turn_left()

def turn_around():
    for i in range(2):
        hubo.turn_left()

def len_of_num(num):
    num_len = 0
    while num != 0:
        num //= 10
        num_len += 1
    return num_len

def num_of_digits():
    num_len = 0
    while not hubo.on_beeper():
        hubo.move()
    while hubo.front_is_clear():
        num_len += 1
        hubo.move()
    num_len += 1
    return num_len

def calculate_num(num_len):
    num_val = 0
    for i in range(num_len):
        num_of_beepers = 0

        while hubo.on_beeper():
            hubo.pick_beeper()
            num_of_beepers += 1

        num_val += num_of_beepers * (10 ** i)
        hubo.move()
    return num_val

