def isPrime(number):
    for i in range(2,number): #2~number-1까지 정수 생성
        if (number % i == 0):
            return False
    return True

def main(a):
    primeNumbers = 0
    compositeNumbers = 0
    for element in a:
        if (isPrime(element)):
            primeNumbers += 1
        else:
            compositeNumbers += 1
    print("Prime numbers: %d" %primeNumbers)
    print("Composite numbers: %d" %compositeNumbers)

a = [4, 3, 2, 9, 7, 18, 22, 13, 6, 24, 37, 12]
main(a)

a = [2, 4, 6, 8, 10, 12, 16, 37, 74]
main(a)