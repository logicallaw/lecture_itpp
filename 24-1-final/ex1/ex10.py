import cs1graphics as cg

# 캔버스 생성
canvas = cg.Canvas(400, 400, 'white', 'Rabbit Mouth Example')

# 토끼의 작은 입 부분을 구성할 선과 곡선 생성

# 세로 선
vertical_line = cg.Path(cg.Point(200, 195), cg.Point(200, 205))
vertical_line.setBorderWidth(2)

# 왼쪽 곡선
left_curve = cg.Path(cg.Point(200, 205), cg.Point(195, 210), cg.Point(190, 205))
left_curve.setBorderWidth(2)

# 오른쪽 곡선
right_curve = cg.Path(cg.Point(200, 205), cg.Point(205, 210), cg.Point(210, 205))
right_curve.setBorderWidth(2)

# 캔버스에 추가
canvas.add(vertical_line)
canvas.add(left_curve)
canvas.add(right_curve)

# 프로그램이 종료되지 않도록 대기
canvas.wait()
