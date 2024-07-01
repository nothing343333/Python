user_input = input("enter your text\n")
if " " in user_input:
    result = user_input.replace(" ", "...")
    print(result)