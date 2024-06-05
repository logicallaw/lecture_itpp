def find_max(numbers):
    max = numbers[0]
    for number in numbers:
        if number > max :
            max = number
    return max

numbers = [0,4,5,6,2,2,1,4,5]
print(find_max(numbers))