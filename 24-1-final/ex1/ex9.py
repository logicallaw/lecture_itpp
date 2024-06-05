from cs1graphics import *
from math import *

# 캔버스 생성
canvas = Canvas(400, 300, 'sky blue', 'Sunny Day')

# 태양 본체
sun = Circle(40, Point(100, 100))
sun.setFillColor('yellow')
canvas.add(sun)

# 태양 광선 그리기
for angle in range(0, 360, 15):  # 15도 간격으로 광선을 추가
    # 각 광선은 시계방했을 선분으로 정의
    ray = Path(Point(100, 100), Point(100 + 60 * cos(angle*pi/180), 100 + 60 * sin(angle*pi/180)))
    ray.setBorderColor('yellow')
    ray.setBorderWidth(3)
    print("hi")
    canvas.add(ray)

# 화면 보여 주기
canvas.wait()