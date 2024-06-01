def summation(n):
   return 1 if (n == 0 or n == 1)  else n + summation(n-1)

num = 5
print("", summation(num))