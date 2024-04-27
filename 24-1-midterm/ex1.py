from cs1robots import * #cs1robots 라이브러리의 모든 것을 불러와라.

create_world() #map 불러온다.
hubo = Robot() #객체 생성
hubo.set_trace("blue") #휴보의 지나가는 길을 색으로 표현한다.
hubo.set_pause(0.3)
#beepers : 동전의 개수, 동전을 지니게 된다.

hubo.move()
hubo.turn_left()
hubo.move()
hubo.turn_left()
hubo.move()
hubo.turn_left()
hubo.move()
hubo.turn_left()
