# دریافت دو عدد a و b
a, b = map(int, input().split())


# محاسبه ب.م.م با الگوریتم اقلیدس
def gcd(x, y):
    while y:
        x, y = y, x % y
    return x


print(gcd(a, b))
