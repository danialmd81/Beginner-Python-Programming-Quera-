n = int(input())
weights = list(map(int, input().split()))
watermelons = [(i + 1, weights[i]) for i in range(n)]

while len(watermelons) > 1:
    # دو هندوانه با کمترین شماره
    wm1, wm2 = watermelons[0], watermelons[1]
    # حذف مرحله‌ای هندوانه سبک‌تر
    if wm1[1] < wm2[1]:
        del watermelons[0]
    else:
        del watermelons[1]

print(watermelons[0][0])
