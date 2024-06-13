from cs1robots import *
def len_of_num(num):
    count = 0
    while num != 0: #123, 12, 1
        num //= 10
        count += 1
    return count

def num_of_digits():
    count = 0
    while not hubo.on_beeper():
        hubo.move()
    while hubo.front_is_clear():
        hubo.move()
        count += 1
    count += 1
    return count

def calculate_num(num_len):
    result = 0
    for i in range(num_len):
        temp = 0
        while hubo.on_beeper():
            hubo.pick_beeper()
            temp += 1
        hubo.move()
        result += temp * (10 ** i)
    return result

def turn_around():
    for i in range(2):
        hubo.turn_left()

def move_to_wall():
    while hubo.front_is_clear():
        hubo.move()

load_world("../worlds/add1.wld")
hubo = Robot(street = 2)

num1_len = num_of_digits()
turn_around()
num1 = calculate_num(num1_len)
move_to_wall()

hubo.turn_left()
hubo.move()
hubo.turn_left()

num2_len = num_of_digits()
turn_around()
num2 = calculate_num(num2_len)
turn_around()
move_to_wall()
turn_around()

num3 = num1 + num2
num3_len = len_of_num(num3)

tmp_num3 = num3
for i in range(num3_len):
    remainder = tmp_num3 % 10
    tmp_num3 //= 10
    for i in range(remainder):
        hubo.drop_beeper()
    hubo.move()