# 4. Write a program to find whether a given number is prime or not.
def prime(x):
    if(x%x == 0 and x%1 == 0 and x%2!=0):
        print("It is prime\n") 
    else:
        print("It is not a prime\n")

x = int(input("Enter a number: "))
prime(x)
