weights = list(map(int, input().split()))
watermelons = [(i + 1, w) for i, w in enumerate(weights)]

while len(watermelons) > 1:
    # دو هندوانه با کمترین شماره را انتخاب کن
    watermelons.sort()
    a, b = watermelons[0], watermelons[1]
    # هندوانه سبک‌تر را حذف کن
    if a[1] < b[1]:
        del watermelons[0]
    else:
        del watermelons[1]

print(watermelons[0][0])
