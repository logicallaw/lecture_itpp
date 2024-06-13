text = "My birthday is 1988/04/29."
print(text.split('/'))

result1 = ['My birthday is 1988', '04', '29.']
result2 = ['My', 'birthday', 'is', '1988/04/29.']

print("/".join(result1))
print(" ".join(result2))
string = "abcde"
print("-".join(string))
print(" ".join(string))
