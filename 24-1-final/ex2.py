from cs1graphics import *
canvas = Canvas(400, 400)
canvas.setBackgroundColor("light blue")
canvas.setTitle("Final Exam")

smile = Layer()
yellow_face = Circle(100, Point(200, 200))
yellow_face.setFillColor("yellow")
yellow_face.setDepth(40)
smile.add(yellow_face)

leye = Circle(10, Point(160, 180))
leye.setFillColor("black")
leye.setDepth(10)
smile.add(leye)

reye = Circle(10, Point(240, 180))
reye.setFillColor("black")
reye.setDepth(10)
smile.add(reye)

mouth = Circle(70, Point(200, 220))
mouth.setFillColor("black")
mouth.setDepth(30)
smile.add(mouth)

eliminate_mouth = Rectangle(140, 70, Point(200, 185))
eliminate_mouth.setFillColor("yellow")
eliminate_mouth.setBorderColor("yellow")
eliminate_mouth.setDepth(20)
smile.add(eliminate_mouth)
# leye, reye/eliminate_mouth/mouth/face

r = Square(50, Point(200, 185))
r.setFillColor('white')
r.setDepth(2)
r.setBorderWidth(0)
smile.add(r)

q = Square(30, Point(240, 145))
q.setFillColor('light gray')
q.setDepth(1)
q.setBorderWidth(0)
smile.add(q)
canvas.add(smile)