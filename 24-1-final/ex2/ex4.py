text = "My Birthday is 1988/04/29"
result1 = text.split("/")
result2 = text.split()
print(result1)
print(result2)

text1 = "/".join(result1)
text2 = " ".join(result2)

print(text1)
print(text2)

string = "abcde"
str_join1 = "-".join(string)
str_join2 = " ".join(string)
print(str_join1)
print(str_join2)