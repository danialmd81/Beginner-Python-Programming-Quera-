from collections import Counter

S = input().strip()
P = input().strip()
n, m = len(S), len(P)
ans = 0
p_count = Counter(P)

for i in range(n - m + 1):
    sub = S[i : i + m]
    sub_count = Counter(sub)
    q = sub_count.get("?", 0)
    # تعداد کمبود هر حرف نسبت به P
    need = 0
    for ch in p_count:
        diff = p_count[ch] - sub_count.get(ch, 0)
        if diff > 0:
            need += diff
    # اگر تعداد ? کافی بود و هیچ حرف اضافه‌ای غیر از ? نداشت
    extra = sum(sub_count[ch] for ch in sub_count if ch != "?" and ch not in p_count)
    if need <= q and extra == 0:
        ans += 1

print(ans)
