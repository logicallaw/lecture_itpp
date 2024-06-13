# 딕셔너리 생성 예시
my_dict = {'CS': 'Computer Science', 'EE': 'Electrical Engineering', 'MAS': 'Mathematical Sciences'}

# dict() 함수를 사용한 생성
my_dict2 = dict(CS='Computer Science', EE='Electrical Engineering', MAS='Mathematical Sciences')

# print(my_dict.keys())
# print(my_dict.values())
# print(my_dict.items())

# # 값 접근
# print(my_dict['CS'])  # 출력: Computer Science
#
# # 값 수정
# my_dict['CS'] = 'CompSci'
# print(my_dict['CS'])  # 출력: CompSci
#
# # 새로운 키-값 쌍 추가
# my_dict['ME'] = 'Mechanical Engineering'
# print(my_dict)  # 출력: {'CS': 'CompSci', 'EE': 'Electrical Engineering', 'MAS': 'Mathematical Sciences', 'ME': 'Mechanical Engineering'}: {'CS': 'CompSci', 'EE': 'Electrical Engineering', 'ME': 'Mechanical Engineering', 'PH': 'Physics', 'BIO': 'Biology'

# 키 반복
for key in my_dict:
    print(key, my_dict[key])

# 키와 값 반복
for key, value in my_dict.items():
    print(f'{key}: {value}')