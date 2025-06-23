# دریافت دو عدد سه رقمی
num1 = input()
num2 = input()

# معکوس کردن اعداد
rev1 = int(num1[::-1])
rev2 = int(num2[::-1])

# مقایسه و چاپ خروجی
if rev1 < rev2:
    print(f"{num1} < {num2}")
elif rev1 > rev2:
    print(f"{num2} < {num1}")
else:
    print(f"{num1} = {num2}")
