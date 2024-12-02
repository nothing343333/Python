# 4. Write a recursive function to calculate the sum of first n natural numbers.
def addition(x):
    if x == 0 or x == 1:
        return 1
    else:
        return x+addition(x-1)
x = int(input("Enter any numeric value\n"))
print(addition(x))