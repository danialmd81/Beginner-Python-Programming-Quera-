# دریافت عدد n به صورت رشته
n = input().strip()
while len(n) > 1:
    n = str(sum(int(d) for d in n))
print(n)
