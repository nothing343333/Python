# 1. Write a program using functions to find greatest of three numbers
def great(a,b,c):
    max = 0
    if a>b and a>c:
        max = a
    elif b>a and b>c:
        max = b
    elif c>a and c>b:
        max = c
    return max

print(great(1,2,3))
