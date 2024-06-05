from cs1robots import *
load_world("../worlds/add1.wld")
hubo = Robot(street = 2)

row2 = []
row1 = []
result = [0,0,0,0,0]

def turn_right():
    for i in range(3):
        hubo.turn_left()

while hubo.front_is_clear():
    cnt = 0
    while hubo.on_beeper():
        hubo.pick_beeper()
        cnt += 1
    hubo.move()
    row2.append(cnt)

cnt = 0
while hubo.on_beeper():
    hubo.pick_beeper()
    cnt += 1
row2.append(cnt)

turn_right()
hubo.move()
turn_right()
for i in range(4):
    cnt = 0
    while hubo.on_beeper():
        cnt += 1
        hubo.pick_beeper()
    row1.append(cnt)
    hubo.move()

row2.reverse()
print(row2)
print(row1)

for i in range(4):
    r = row1[i] + row2[i]
    if r > 9 :
        result[i + 1] += r % 10
    else:
        result[i] = r


for r in result:
    print(r)