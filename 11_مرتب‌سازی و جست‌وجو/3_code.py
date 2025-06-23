n = int(input())
nums = list(map(int, input().split()))
print(sum(range(1, n + 1)) - sum(nums))
