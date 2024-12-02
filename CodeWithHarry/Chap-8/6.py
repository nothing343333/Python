# 6. Write a python function which converts inches to cms.
def convert(x):
    return x*2.54

x = int(input("Enter numeric value\n"))
print(f"inches into cm {x} = {convert(x)}")