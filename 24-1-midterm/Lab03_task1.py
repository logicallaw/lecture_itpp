results = [55,90,89,76,37,100,67]
counter = 0;
for result in results:
    counter+=1
    if (90 <= result):
        print("%d번 학생은 %d점으로 A입니다." %(counter, result))
    elif (80<= result):
        print("%d번 학생은 %d점으로 B입니다." % (counter, result))
    elif (70<= result):
        print("%d번 학생은 %d점으로 C입니다." % (counter, result))
    elif (60<= result):
        print("%d번 학생은 %d점으로 D입니다." % (counter, result))
    else:
        print("%d번 학생은 %d점으로 F입니다." % (counter, result))