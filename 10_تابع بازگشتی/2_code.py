n = int(input())
a, b = 1, 1
s = 0
for i in range(n):
    s += a
    a, b = b, a + b
print(s)
