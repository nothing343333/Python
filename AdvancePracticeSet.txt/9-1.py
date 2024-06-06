dem = open("Poems.txt", mode="r")
demdo = dem.read()
if "twinkle" in demdo:
    print("Yes!!")
else:
    print("Sorry absent!")
find = dem.close