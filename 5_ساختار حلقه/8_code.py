# عدد کامل عددی است که مجموع مقسوم‌علیه‌های صحیح و مثبتش (به جز خودش) برابر خودش باشد
n = int(input())
sum_div = 0
for i in range(1, n // 2 + 1):
    if n % i == 0:
        sum_div += i
if sum_div == n:
    print("YES")
else:
    print("NO")
