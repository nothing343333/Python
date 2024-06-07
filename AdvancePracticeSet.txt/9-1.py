dem = open("Poems.txt", mode="r")
demdo = dem.read()
if "twinkle" in demdo:
    print("Twinkle is present\n")
else:
    print("Twinkle is not present\n")
find = dem.close