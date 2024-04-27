result = [55, 90, 89, 76, 37, 100, 67]
for i in result:
    if i >= 90:
        grade = "A"
    elif i >= 80:
        grade = "B"
    elif i >= 70:
        grade = "C"
    elif i >= 60:
        grade = "D"
    else:
        grade = "F"
    print("%d번 학생은 %d점으로 %s입니다." % (i + 1, i, grade))