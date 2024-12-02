# 1. Write a program to print multiplication table of a given number using for loop.
x = int(input("Enter any number\n"))
for i in range(10):
    print(f"{x} x {i} = {i*x}")
    i=i+1