from cs1graphics import *
import time
canvas = Canvas(400, 300)
canvas.setBackgroundColor((100,100,100))
canvas.setTitle("Lunar")

Lanar = Circle(100)
Lanar.setFillColor('yellow')
Lanar.moveTo(200,150)
canvas.add(Lanar)

Black = Circle(100)
Black.setFillColor('black')
Black.moveTo(0,150)
canvas.add(Black)

for i in range(100):
    time.sleep(0.1)
    Black.move(2,0)