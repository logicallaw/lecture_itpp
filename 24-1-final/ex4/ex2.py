from cs1graphics import *
canvas = Canvas(400, 400)
canvas.setBackgroundColor('light blue')
canvas.setTitle('Final Exam')
smile = Layer()

yellow_face = Circle(100, Point(200, 200))
yellow_face.setFillColor('yellow')
yellow_face.setDepth(4)
smile.add(yellow_face)

leye = Circle(10, Point(160, 180))
leye.setFillColor('black')
leye.setDepth(1)
smile.add(leye)

reye = Circle(10, Point(240, 180))
reye.setFillColor('black')
reye.setDepth(1)
smile.add(reye)

mouth = Circle(70, Point(200, 220))
mouth.setFillColor('black')
mouth.setDepth(3)
smile.add(mouth)

eliminate_mouth = Rectangle(140, 70, Point(200, 185))
eliminate_mouth.setFillColor('yellow')
eliminate_mouth.setBorderColor('yellow')
eliminate_mouth.setDepth(2)
smile.add(eliminate_mouth)

canvas.add(smile)
