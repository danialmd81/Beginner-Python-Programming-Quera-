n, x = map(int, input().split())
a = list(map(int, input().split()))
x = x % n  # برای جلوگیری از چرخش‌های اضافی
result = a[-x:] + a[:-x] if x != 0 else a
print(" ".join(map(str, result)))
