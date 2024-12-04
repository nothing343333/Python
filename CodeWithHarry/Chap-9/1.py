# 1. Write a program to read the text from a given file ‘poems.txt’ and find out
# whether it contains the word ‘twinkle’.

f = open("poems.txt", mode="r")
content = f.read()
if("twinkle" in content):
    print("Yes it contains twinkle\n")
else:
    print("No it does not contain twinkle\n")
f.close()