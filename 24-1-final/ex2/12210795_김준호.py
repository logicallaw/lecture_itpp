from cs1graphics import *
from time import *
#paper
paper = Canvas()
paper.setBackgroundColor("lightgreen")
paper.setTitle("Hi, Fu Bao!")
paper.setWidth(450)
paper.setHeight(350)

#meadow
meadow = Rectangle(600, 150, Point(300, 300))
meadow.setFillColor('green')
paper.add(meadow)

#sun
sun = Circle(50, Point(400, 50))
sun.setFillColor('yellow')
paper.add(sun)

#fubao
fubao = Layer()

#fubao:body
body_back = Circle(52, Point(100,200))
body_back.setFillColor('white')
fubao.add(body_back)

body_front = Circle(40, Point(100, 200))
body_front.setFillColor('black')
fubao.add(body_front)

#fubao:head
head = Circle(35, Point(100, 150))
head.setFillColor('white')
fubao.add(head)

#fubao:face
L = Circle(6, Point(90,145))
L.setFillColor('black')
fubao.add(L)

R = Circle(6, Point(110,145))
R.setFillColor('black')
fubao.add(R)

eyeL = Circle(2, Point(90, 145))
eyeL.setFillColor('white')
fubao.add(eyeL)

eyeR = Circle(2, Point(110, 145))
eyeR.setFillColor('white')
fubao.add(eyeR)

nose = Polygon(Point(100, 170), Point(95, 160), Point(104, 160))
nose.setFillColor('black')
fubao.add(nose)

#fubao:ear
earL = Circle(10, Point(80, 120))
earL.setFillColor('black')
fubao.add(earL)

earR = Circle(10, Point(120, 120))
earR.setFillColor('black')
fubao.add(earR)

#fubo:mouth
mouth = Path(Point(90, 173), Point(110, 173))
mouth.setBorderWidth(2)
fubao.add(mouth)

#fubo:arm
armL = Circle(15, Point(40, 180))
armL.setFillColor('black')
fubao.add(armL)

armR = Circle(15, Point(155, 180))
armR.setFillColor('black')
fubao.add(armR)

#fubo:leg
legL = Circle(15, Point(70, 260))
legL.setFillColor('black')
fubao.add(legL)

legR = Circle(15, Point(130, 260))
legR.setFillColor('black')
fubao.add(legR)
paper.add(fubao)

#fubao moves to 159, 20
timeDelay = 0.3
fubao.moveTo(150,20)

#fubao eat some bamboo
bamboo = Rectangle(10, 60, Point(250, 220))
bamboo.setFillColor('green')
paper.add(bamboo)

for i in range(10):
    sleep(timeDelay)
    bamboo.move(0, -2)  # x축으로 -5, y축으로 -1 이동
    bamboo.scale(0.9)  # 높이를 90%로 줄임
paper.remove(bamboo)

text = Text("Fubao is happy!", 15, Point(150, 50))
text.setFontColor('black')
paper.add(text)