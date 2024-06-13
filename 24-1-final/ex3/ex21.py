def add_attendance(attendance_set, name):
    attendance_set.add(name)

def check_attendance(attendance_set, name):
    return name in attendance_set

def remove_attendance(attendance_set, name):
    attendance_set.remove(name)

def print_all_attendance(attendance_set):
    for i in attendance_set:
        print(i)
def intersection_attendance(attendance_set1, attendance_set2):
    return attendance_set1.intersection(attendance_set2)

def union_attendance(attendance_set1, attendance_set2):
    return attendance_set1.union(attendance_set2)

def difference_attendance(attendance_set1, attendance_set2):
    return attendance_set1.difference(attendance_set2)


attendance = set()

# 출석 추가
add_attendance(attendance, "Alice")
add_attendance(attendance, "Bob")
add_attendance(attendance, "Charlie")

# 모든 출석 학생 출력
print_all_attendance(attendance)

# 출석 확인
check = check_attendance(attendance, "Alice")
print(f"Alice's attendance: {check}")

# 출석 삭제
remove_attendance(attendance, "Bob")

# 모든 출석 학생 출력
print_all_attendance(attendance)

# 다른 출석 집합과의 교집합, 합집합, 차집합
attendance_set2 = {"Charlie", "Alice", "Eve"}

intersection_attendance(attendance, attendance_set2)
union_attendance(attendance, attendance_set2)
difference_attendance(attendance, attendance_set2)

