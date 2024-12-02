# 2. Write a python program using function to convert Celsius to Fahrenheit
def temp(x):
    return (x*1.8)+32

x = int(input("Enter temprature in celcius\n"))
print(f"Temprature in fahrenehit = {temp(x)}")