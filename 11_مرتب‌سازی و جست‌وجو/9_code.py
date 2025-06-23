n = int(input())
nums = list(map(int, input().split()))
m = int(input())

left, right = 0, n - 1
found = -1
while left <= right:
    mid = (left + right) // 2
    if nums[mid] == m:
        found = mid
        break
    elif nums[mid] < m:
        left = mid + 1
    else:
        right = mid - 1

print(found)
