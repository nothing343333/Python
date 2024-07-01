user_input = input("enter your text here\n")
if ":)" in user_input:
    result = user_input.replace(":)", "🙂")
    print(result)
elif ":(" in user_input:
    anotherresult = user_input.replace(":(", "🙁")
    print(anotherresult)