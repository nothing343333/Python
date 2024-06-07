
with open("gamble.txt") as f:
    content = f.read()
content = content.replace("rand", "#$&$%#")
content = content.replace("donkey", "#$&$%#")
content = content.replace("kamina", "#$&$%#")
content = content.replace("gand", "#$&$%#")

with open("gamble.txt", "w") as f:
    f.write(content)