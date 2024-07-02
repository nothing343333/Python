name = input("File Name: ")
if ".jpg" in name or ".gif" in name or "jpeg" in name:
    result = name.replace("jpg", "/jpg")
    print(result)