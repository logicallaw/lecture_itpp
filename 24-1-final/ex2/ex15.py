# def is_triangle(a, b, c):
#     if a>=b:
#         if a>=c:
#             return True if a < b + c else False
#         else:
#             return True if c < a + b else False
#     else:
#         if b>=c:
#             return True if b < a + c else False
#         else:
#             return True if c < a + b else False
def is_triangle(a, b, c):
    if a < b + c or b < a + c or c < a + b:
        return True
    else:
        return False

a = float(input("Side a : "))
b = float(input("Side b : "))
c = float(input("Side c : "))
if is_triangle(a, b, c):
    print("YES")
else:
    print("NO")
