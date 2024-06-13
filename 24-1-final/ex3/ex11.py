def histogram(medals):
    t = [0] * 14
    for item in medals:
        total = sum(item[1:])
        t[total//3] += 1
    for i in range(14):
        print(str(3 * i) + "~" + str(3 * i + 2) + ":\t" + ("*" * t[i]))
bronze = [1, 6, 0, 0,10, 2, 3, 4, 6, 7, 4, 0, 5, 4, 6, 2, 11, 1, 9, 0, 1, 4, 1, 4, 0, 6]