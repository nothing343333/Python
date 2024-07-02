name = input("File Name: ")
if ".jpg" in name:
    result = name.replace(".jpg", "  ")
    final = result.replace(result, " image/jpg")
    print(final)
elif ".png" in name:
    result = name.replace(".png", "  ")
    final = result.replace(result, " image/png")
    print(final)
elif ".jpg" in name:
    result = name.replace(".gif", "  ")
    final = result.replace(result, " image/gif")
    print(final)
    # result = name.replace(".gif", "  ")
    # final = result.replace(result, " image/gif")
    # print(final)
    # result = name.replace(".jpeg", "  ")
    # final = result.replace(result, " image/jpeg")
    # print(final)