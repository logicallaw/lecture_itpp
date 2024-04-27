def early30Minutes(h, m):
    if m >= 30:
        m -= 30
    else:
        if h < 1:
            h = 23
        else:
            h -= 1
        m += 30

    if 0 <= h <= 9 and 0 <= m <= 9:
        print("0%d:0%d" %(h, m))
    elif 0 <= h <= 9 and m >= 10:
        print("0%d:%d" %(h, m))
    elif h >= 10 and 0 <= m <= 9:
        print("%d:0%d" % (h, m))
    else:
        print("%d:%d" % (h, m))


early30Minutes(10,45)
early30Minutes(9,30)
early30Minutes(3,20)
early30Minutes(11,10)
early30Minutes(0,23)