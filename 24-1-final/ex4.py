import math
def grade_calculator(grade):
    #all scores, average, stdv, max grade, min grade
    sum = 0
    for g in grade:
        sum += g
        print(g, end= " ")
    avg = sum / len(grade)
    print("\naverage:%.2f" % avg)

    temp = 0
    for g in grade:
        temp += (g - avg) ** 2
    standard_deviation = math.sqrt(temp / len(grade))
    print("standard deviation:%.2f" % standard_deviation)
    print("max:%d, min:%d" %(max(grade), min(grade)))

def student_grade(num):
    grades = []
    for i in range(int(num)):
        user_input = int(input("Enter grade: "))
        grades.append(user_input)
    return grades

while True:
    studentNum = input("학생 수를 입력하세요:")
    if int(studentNum) > 0 and int(studentNum) <= 10:
        break
    else:
        print("다시입력하세요")

studentGrade = student_grade(studentNum)
grade_calculator(studentGrade)