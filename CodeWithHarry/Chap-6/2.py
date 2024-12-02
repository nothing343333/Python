# 2. Write a program to find out whether a student has passed or failed if it requires a
# total of 40% and at least 33% in each subject to pass. Assume 3 subjects and
# take marks as an input from the user.

x = int(input("enter maths marks\n"))
y = int(input("enter eng marks\n"))
z = int(input("enter bio marks\n"))
if((x>= 33 and y>= 33 and z>=33)):
        if((x+y+z)/3 >= 40):
                print("Passed\n")
else:
        print("Failed\n")