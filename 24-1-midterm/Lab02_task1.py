def isSamePoints(x1,y1,x2,y2):
    if (x1 == x2) & (y1 == y2):
        return True
    else:
        return False

def isXaxisSymmetry(x1,y1,x2,y2):
    if (x1 == -x2) & (y1 == y2):
        return True
    else:
        return False

def isYaxisSymmetry(x1,y1,x2,y2):
    if (x1 == x2) & (y1 == -y2):
        return True
    else:
        return False

def isOriginSymmetry(x1,y1,x2,y2):
    if (x1 == -x2) & (y1 == -y2):
        return True
    else:
        return False

def printType(x1,y1,x2,y2):
    if isSamePoints(x1,y1,x2,y2):
        print("The same points")
    elif isXaxisSymmetry(x1,y1,x2,y2):
        print("X-axis symmetry")
    elif isYaxisSymmetry(x1,y1,x2,y2):
        print("Y-axis symmetry")
    elif isOriginSymmetry(x1,y1,x2,y2):
        print("Origin symmetry")
    else:
        print("Nothing")

a = (5, 5)
b = (-5, 5)
printType(a[0],a[1],b[0],b[1])

a = (3, 3)
b = (7, -3)
printType(a[0],a[1],b[0],b[1])
