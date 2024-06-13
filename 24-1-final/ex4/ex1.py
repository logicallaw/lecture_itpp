from cs1graphics import *
canvas = Canvas(400, 400)
canvas.setBackgroundColor('light blue')
canvas.setTitle("Final Exam")

face = Layer()
Large_cir = Circle(100, Point(200, 200))
Large_cir.setFillColor('blue')
face.add(Large_cir)

small_cir = Circle(30, Point(200, 120))
small_cir.setFillColor('red')
face.add(small_cir)

left_eye = Circle(10, Point(170, 180))
left_eye.setFillColor('black')
face.add(left_eye)

right_eye = Circle(10, Point(230, 180))
right_eye.setFillColor('black')
face.add(right_eye)

half_cir = Circle(50, Point(200, 240))
half_cir.setFillColor('black')
face.add(half_cir)

rect = Rectangle(100, 50, Point(200, 265))
rect.setFillColor('blue')
rect.setBorderWidth(0)
face.add(rect)

canvas.add(face)