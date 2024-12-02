# 5. Write a program to find the sum of first n natural numbers using while loop.
x = int(input("Enter any number\n"))
sum = 0
i = 1
while i <= x:
    sum += i
    i += 1
print(sum)