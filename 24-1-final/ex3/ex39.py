numbers = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]
fruits = ["apple", "banana", "cherry", "date"]

numbers.append(7)
print(numbers)
numbers.sort()
print(numbers)

ll = set(numbers)
numbers = list(ll)
numbers.sort()
print(numbers)

fruits.remove('banana')
print(fruits)

date_index = fruits.index('date')
fruits.insert(date_index + 1, "elderberry")
print(fruits)