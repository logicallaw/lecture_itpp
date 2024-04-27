def early30Minute(h, m):
    if (m - 30 < 0):
        if(h - 1 < 0):
            h = 23
        else:
            h -= 1
        m = 30 + m
    else:
        m -= 30
    if ((h < 10) and (m < 10)):
        print("0%d:0%d" % (h, m))
    elif ((h > 10) and (m < 10)):
        print("%d:0%d" % (h, m))
    elif ((h < 10) and (m > 10)):
        print("0%d:%d" % (h, m))
    else:
        print("%d:%d" % (h, m))

hour = 10
minute = 45
early30Minute(hour,minute)

hour = 9
minute = 30
early30Minute(hour,minute)

hour = 3
minute = 20
early30Minute(hour,minute)

hour = 11
minute = 10
early30Minute(hour,minute)

hour = 0
minute = 23
early30Minute(hour,minute)
