# 6. Write a program to calculate the grade of a student from his marks from the
# following scheme:
# 90 – 100 => Ex
# 80 – 90 => A
# 70 – 80 => B
# 60 – 70 =>C
# 50 – 60 => D
# <50 => F

x = int(input("Enter marks of bio\n"))
y = int(input("Enter marks of maths\n"))
z = int(input("Enter marks of english\n"))
result = (x+y+z)/3
if result == 100 or result>=90:
    print("Ex\n")
elif result>=80:
    print("A\n")
elif result>=70:
    print("B\n")
elif result>=60:
    print("C\n")
elif result>=50:
    print("D\n")
