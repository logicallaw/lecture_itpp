s1 = set([1,2,3,4,5,6])
s2 = set([4,5,6,7,8,9])
s3 = s1.intersection(s2)
print(s3)

s4 = s1 | s2
print(s4)
print(s1.union(s2))

print(s1 - s2)
print(s1.difference(s2))
print(s2.difference(s1))