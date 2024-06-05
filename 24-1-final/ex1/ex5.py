from cs1graphics import *

# 캔버스 생성
canvas = Canvas(400, 300, 'lightblue', 'Cute Bear')

panda = Layer()

background = Rectangle()
b = Circle(52, Point(200, 200))
b.setFillColor('white')
panda.add(b)
# 곰의 몸체
body = Circle(40, Point(200, 200))
body.setFillColor('black')
# body.setDepth(10)
panda.add(body)



# 곰의 머리
head = Circle(35, Point(200, 150))
head.setFillColor('white')
panda.add(head)

# 왼쪽 귀
left_ear = Circle(10, Point(185, 120))
left_ear.setFillColor('black')
panda.add(left_ear)

# 오른쪽 귀
right_ear = Circle(10, Point(215, 120))
right_ear.setFillColor('black')
panda.add(right_ear)

# 눈
left_eye = Circle(5, Point(190, 145))
left_eye.setFillColor('black')
panda.add(left_eye)

right_eye = Circle(5, Point(210, 145))
right_eye.setFillColor('black')
panda.add(right_eye)

l = Circle(2, Point(190, 145))
l.setFillColor('white')
panda.add(l)

r = Circle(2, Point(210, 145))
r.setFillColor('white')
panda.add(r)
# 코
nose = Circle(5, Point(200, 160))
nose.setFillColor('black')
panda.add(nose)

# 입
mouth = Path(Point(195, 165), Point(200, 170), Point(205, 165))
mouth.setBorderColor('black')
panda.add(mouth)

meadow = Rectangle(600, 200, Point(300, 300))
meadow.setFillColor('green')
canvas.add(meadow)


# 화면 보여 주기
canvas.add(panda)
canvas.wait()