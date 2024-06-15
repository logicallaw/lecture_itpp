list1 = ["A","B","C"]
list2 = list1
list2.append("D")
list1[2] = "E"
print(len(list1))
print(len(list2))
print(list1 == list2)