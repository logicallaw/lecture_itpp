from cs1graphics import *

# 캔버스 생성
canvas = Canvas(600, 400, 'sky blue', 'Bamboo on a Green Meadow')

# 푸른 초원 그리기
meadow = Rectangle(600, 200, Point(300, 300))
meadow.setFillColor('green')
canvas.add(meadow)


# 대나무 그리기
def draw_bamboo(x, y):
    # 대나무 줄기
    for i in range(5):
        segment = Rectangle(20, 40, Point(x, y - 40 * i))
        segment.setFillColor('light green')
        canvas.add(segment)

        # 대나무 마디
        joint = Circle(10, Point(x, y - 40 * i - 20))
        joint.setFillColor('dark green')
        canvas.add(joint)

    # 대나무 잎
    leaf1 = Path(Point(x, y - 200), Point(x + 15, y - 215), Point(x, y - 230))
    leaf1.setBorderColor('dark green')
    leaf1.setBorderWidth(3)
    canvas.add(leaf1)

    leaf2 = Path(Point(x, y - 200), Point(x - 15, y - 215), Point(x, y - 230))
    leaf2.setBorderColor('dark green')
    leaf2.setBorderWidth(3)
    canvas.add(leaf2)


# 여러 대나무 그리기
draw_bamboo(200, 350)
draw_bamboo(240, 350)
draw_bamboo(280, 350)
draw_bamboo(320, 350)
draw_bamboo(360, 350)
draw_bamboo(400, 350)

# 화면 보여 주기
canvas.wait()