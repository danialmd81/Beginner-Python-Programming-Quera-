n = int(input())
nums = list(map(int, input().split()))
m = int(input())
indices = [i for i, num in enumerate(nums) if num == m]
if indices:
    print(*indices)
else:
    print(-1)
