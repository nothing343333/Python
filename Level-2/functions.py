# functions
# def greet():
#     print("Hello from function")

# # calling a funtion
# # greet()
# print("Hello ", greet())


# def add_numbers(x, y):
#     result = x+y
#     print("Sum", result)

# add_numbers(5, 5)









# def greet_user(username):
#     print(f"Hello, {username}, How are you doing?")

# greet_user("HuXn")






# def greet_person(name, greetings="Hello!"):
    # print(f"{greetings}, {name}")

# greet_person("HuXn")
# greet_person("HuXn", "Heyy sexyy")





#
# def outer_function(x):
#     """Outer function with a nested function."""

#     def inner_function(y):
#         """Inner function."""
#         return x + y

#     result = inner_function(5)
#     return result

# # Calling the outer function
# result_value = outer_function(10)
# print("Result:", result_value)









# lambda arguments: expression

# add = lambda x, y: x + y
# result = add(3, 5)
# print(result)  # Output: 8


# Function that takes another function as an argument
# def apply_operation(x, y, operation):
#     return operation(x, y)

# result_addition = apply_operation(5, 3, lambda a, b: a + b)
# print("Result of addition:", result_addition)

# result_multiplication = apply_operation(5, 3, lambda a, b: a * b)
# print("Result of multiplication:", result_multiplication)