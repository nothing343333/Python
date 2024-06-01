# to find weather the input is a prime number or not
prime = int(input("enter the value which you want to find as prime or not\n"))
 
if prime%prime == 0 and prime%1 == 0 and prime%2 != 0  or prime == 2:
    print("The following is a prime number\n")
else:
    print("The following is not a prime number\n")