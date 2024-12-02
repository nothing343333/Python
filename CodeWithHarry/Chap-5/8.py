# 8. If languages of two friends are same; what will happen to the program in problem
# 6?
favLang = {}
for i in range(4):
    name = input(f"Enter friend {i+1}'s name: ")
    lang = input(f"Enter {name}'s favorite language: ")
    favLang[name] = lang
print("\nFriends' favorite languages:")
for name, lang in favLang.items():
    print(f"{name}'s favorite language is {lang}")
    #it will not affact anything