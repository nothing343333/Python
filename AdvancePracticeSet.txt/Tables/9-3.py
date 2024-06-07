# i = 0
# for i in range(10):
#     print(f"5x{i+1}=",5*(i+1))
#     i = i+1

for i in range(2, 21):
    with open(f"Tables{i}", "w") as f:
        
        for j in range(1,11):
                f.write(f"{i}x{j}={i*j}\n")
        if j!=10:
            f.write("\n")

