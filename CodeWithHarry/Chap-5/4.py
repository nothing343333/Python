# 4. What will be the length of following set s:
s = set()
s.add(20)
s.add(20.0)
s.add('20') # length of s after these operations?
print(len(s))
# it will cosnider 20 and 20.0 as one as values are same