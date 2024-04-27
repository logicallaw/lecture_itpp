from cs1media import *
img = load_picture("img/a.png")
threshold1 = 255/3
threshold2 = threshold1 * 2
w, h = img.size()
for y in range(h):
    for x in range(w):
        r,g,b = img.get(x,y)
        img.set(x,y,(255-r, 255-g, 255-b))
img.show()
