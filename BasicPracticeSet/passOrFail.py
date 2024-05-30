chemistry = int(input("enter marks of chemistry\n"))
biology = int(input("enter marks of biology\n"))
english = int(input("enter the amrks of english\n"))
maths = int(input("enter marks of maths\n"))

if int(chemistry+biology+english+maths)/4 < 40:
    print("Pass\n")

elif chemistry < 33 and biology < 33 and english < 33 and maths < 33:
    print("Pass\n")

else:
    print("Fail\n")