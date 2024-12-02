# 6. Create an empty dictionary. Allow 4 friends to enter their favorite language as
# value and use key as their names. Assume that the names are unique.
favLang = {}
for i in range(4):
    name = input(f"Enter friend {i+1}'s name: ")
    lang = input(f"Enter {name}'s favorite language: ")
    favLang[name] = lang
print("\nFriends' favorite languages:")
for name, lang in favLang.items():
    print(f"{name}'s favorite language is {lang}")