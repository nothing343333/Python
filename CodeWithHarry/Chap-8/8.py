# 8. Write a python function to print multiplication table of a given number.
def table(x):
    for i in range(10):
        i=i+1
        print(f"{x} x {i} = {x*i}")



print(table(5))