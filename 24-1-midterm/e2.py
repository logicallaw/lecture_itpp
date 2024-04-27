list = [100,90,80,55,95,80,65,75,70,90]
sum = 0
for l in list:
    sum+=l
avg = sum/len(list)
s = 0
for l in list:
    print("l:%d, l^2:%d" %(l, l**1/2))
    s += (l-avg)**2
s /= len(list)
print("Means:%d" %avg)
print("Variance:%d" %s)