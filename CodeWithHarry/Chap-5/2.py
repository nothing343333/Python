# 2. Write a program to input eight numbers from the user and display all the unique
# numbers (once).
numbers = set()  
for i in range(8):
    num = int(input(f"Enter number {i+1}: "))
    numbers.add(num)
print("The unique numbers are:", numbers)
