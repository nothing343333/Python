name = input("Enter your name please\n")
name_count = sum(name.count(word) for word in name)
# print("Spam count: ", name_count)
if name_count < 10:
        print("Please enter a name more than 10 characters")