# 1. Write a program to find the greatest of four numbers entered by the user.
a = int(input("enter first value\n"))
b = int(input("enter second value\n"))
c = int(input("enter third value\n"))
d = int(input("enter fourth value\n"))
if(a>b and a>c and a>d):
    print(f"greatest from four = {a}\n")
elif(b>a and b>c and b>d):
    print(f"greatest from four = {b}\n")
elif(c>a and c>b and c>d):
    print(f"greatest from four = {c}\n")
elif(d>a and d>b and d>c):
    print(f"greatest from four = {d}\n")
else:
    print("Invalid operation\n")