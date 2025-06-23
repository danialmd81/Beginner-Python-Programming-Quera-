c1, c2, c3 = input().split()
off = 0
if c1 == "s" or c2 == "s" or c3 == "s":
    off = off + 10
if c1 == "7" or c2 == "7" or c3 == "7":
    off = off + 5
if c1 == "*" or c2 == "*" or c3 == "*":
    off = off + 30
print(int(off))
