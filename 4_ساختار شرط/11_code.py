# دریافت سه کاراکتر
chars = input().split()
# دریافت سه عدد
nums = list(map(int, input().split()))

if chars[0] == chars[1]:
    print(f"Max : {max(nums)}")
elif chars[0] == chars[2]:
    print(f"Min : {min(nums)}")
else:
    print("None")
