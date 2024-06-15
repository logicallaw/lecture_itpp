a = 5
def f(a):
    print("f:",a)

def g():
    global a
    f(a + 11)
    a = a + 17
    print("g:",a)

def h(a):
    a = 99
    g()
    print("h:",a)

print("A:",a) #2
f(13) #13
print("A:",a) #2
g() #f:16,g:22
print("A:",a) #A:22
h(10) #f:33, g:39, h:99
print("A:",a) #A:39