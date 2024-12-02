# 7. Write a program to find out whether a given post is talking about “Harry” or not.
x = str(input("Enter your text\n"))
if("Harry" or "harry" in x):
    print("Yes it contains harry\n")
else:
    print("No it does not contain harry\n")