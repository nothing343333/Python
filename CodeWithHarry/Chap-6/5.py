# 5. Write a program which finds out whether a given name is present in a list or not.
names = ["tirth", "finel", "swetabh", "harkirat", "gimanshu"]
x = str(input("Enter the name you want to find\n"))
if(x in names):
    print("True")
else:
    print("False")