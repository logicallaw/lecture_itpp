from cs1media import *
img = load_picture("img/yuna.jpg")
w,h = img.size()
for y in range(h):
    for x in range(w):
        r,g,b = img.get(x,y)
        v = (r+g+b)//3
        img.set(x,y,(v,v,v))
img.show()