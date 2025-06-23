nums = [float(input()) for _ in range(10)]
avg = sum(nums) / 10
count = sum(1 for x in nums if x > avg)
print(count)
