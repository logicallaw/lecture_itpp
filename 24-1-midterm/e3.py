a = [4,3,2,9,7,18,22,13,6,24,37,12]
counterPrime = 0
counterComposite = 0
b = 0
for element in a:
    for i in range(2, element):
        if element % i == 0:
            b = 1
            break
    if b == 1:
        counterComposite += 1
    else:
        counterPrime += 1

print("Prime numbers: ", counterPrime)
print("Composite numbers: ", counterComposite)