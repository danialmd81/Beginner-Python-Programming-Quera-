t = int(input())
for _ in range(t):
    s = input().strip()
    # شرط ۱: وجود یک رقم که حداقل ۴ بار تکرار شده باشد
    cond1 = any(s.count(d) >= 4 for d in set(s))
    # شرط ۲: وجود سه رقم متوالی یکسان
    cond2 = any(s[i] == s[i + 1] == s[i + 2] for i in range(len(s) - 2))
    # شرط ۳: آینه‌ای بودن شماره
    cond3 = s == s[::-1]
    if cond1 or cond2 or cond3:
        print("Ronde!")
    else:
        print("Rond Nist")
