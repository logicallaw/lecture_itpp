def search(name):
    f = open("students.txt", "r")
    datalst = f.readline()
    for data in datalst:
        if name in data:
            a = data.split("|")
            print("average:%s, grades:%s"%(a[4]), a[5])
            f.close()
            return
    print("없음")
    f.close()