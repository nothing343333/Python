file1 = "dam.txt"
file2 = "gam.txt"
with open(file1) as f:
        f1 = f.read()

with open(file2) as f:
        f2 = f.read()

if f1 == f2:
        print("both are same\n")

else:
        print("files not same\n")