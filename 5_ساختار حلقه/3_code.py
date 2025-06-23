# دریافت دو عدد n و m
n, m = map(int, input().split())

# تولید و چاپ اعداد فرد بین n و m
odds = [str(i) for i in range(n + 1, m) if i % 2 == 1]
print(" ".join(odds))
