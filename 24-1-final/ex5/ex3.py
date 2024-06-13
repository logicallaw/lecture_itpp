text = "My birthday is 1988/04/29."
a = text.split("/")
print(a)

result1 = ['My birthday is 1988', '04', '29.']
result2 = ['My birthday', 'is', '1988/04/29']
r1 = "/".join(result1)
r2 = " ".join(result2)

print(r1)
print(r2)

string = "abcde"

s = " ".join(string)
print(s)