def reverse_number(n):
    n = n.strip()
    if n.startswith("-"):
        return "-" + str(int(n[1:]))[::-1]
    else:
        return str(int(n[::-1]))


nums = []
while True:
    s = input().strip()
    if s == "End":
        break
    nums.append(s)
for i in range(len(nums) - 1, -1, -1):
    print(reverse_number(nums[i]))
