def student(name, mid, fin, assign):
    avg = (mid + fin + assign) / 3
    if avg >= 90:
        score = 'A'
    elif avg >= 80:
        score = "B"
    else:
        score = "C"

    f = open("students.txt",'o')
    data = name + "|" + str(mid) + "|" + str(fin) + "|" + str(assign) + "|" + str(avg) + "|" + score + '\n'
    f.write(data)
    f.close()