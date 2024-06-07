with open("gamble.txt") as f:
    content = f.read()
content = content.replace("donkey", "#$&$%#")

with open("gamble.txt", "w") as f:
    f.write(content)