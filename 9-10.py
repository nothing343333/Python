# f = open("ndtv.text", mode="w")

oldname = "ndtv.text"
newname = "renamed.text"
with open(oldname) as f:
    content = f.read()

with open(newname, "w") as f:
    f.write(content)