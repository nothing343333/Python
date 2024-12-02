# 3. A spam comment is defined as a text containing following keywords:
# “Make a lot of money”, “buy now”, “subscribe this”, “click this”. Write a program
# to detect these spams.
spam = str(input("Enter your mail or text\n"))
if("Make a lot of money" or "buy now" or "subcribe this" or "click this"):
    print("Spam! Be Aware!\n")
else:
    print("Safe.\n")