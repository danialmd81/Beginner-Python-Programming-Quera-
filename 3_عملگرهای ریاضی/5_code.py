h, m = input().split()
h = int(h)
m = int(m)
print("%02d:%02d" % ((12 - h) % 12, (60 - m) % 60))