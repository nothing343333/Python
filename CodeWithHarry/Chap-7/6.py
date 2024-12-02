# 6. Write a program to calculate the factorial of a given number using for loop.
x = int(input("Enter any value\n"))
fact = 1
for i in range(1, x + 1):
    fact *= i
print(fact)