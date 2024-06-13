set1 = {1, 2, 3, 4, 5}
set2 = {4, 5, 6, 7, 8}

union_set1_set2 = set1.union(set2)
print(union_set1_set2)

diff_set1_set2 = set1.difference(set2)
print(diff_set1_set2)

only_set1 = set1.difference(set2)
print(only_set1)

only_set2 = set2.difference(set1)
print(only_set2)

sum_set1_set2 = set1 | set2
print(sum_set1_set2)

set1.add(9)
set1.add(10)
print(set1)
set2.remove(6)
set2.remove(7)
print(set2)